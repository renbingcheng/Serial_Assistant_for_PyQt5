import sys
import time
import serial
import logging
import serial.tools.list_ports
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from qt import qt_ui  # 假设 qt_ui 是从您的 UI 文件生成的
from qt.qt_ui import Ui_mainWindow

# 创建一个新的线程类来处理串口数据的接收
class SerialThread(QThread):
    received_signal = pyqtSignal(bytes)
    error_signal = pyqtSignal(str)  # 报告错误的信号
    opened_signal = pyqtSignal()    # 报告成功打开的信号
    
    def __init__(self, port, baudrate, databits, parity, stopbits, dtr, rts):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.databits = databits
        self.parity = parity
        self.stopbits = stopbits
        self.dtr = dtr
        self.rts = rts
        
        self.serial = None
        self.data_buffer = bytearray()  # 添加一个 bytearray 作为缓冲区

    def run(self):
        try:
            self.serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=self.databits,
                parity=self.parity,
                stopbits=self.stopbits,
                timeout=1
            )
            self.serial.setDTR(self.dtr)
            self.serial.setRTS(self.rts)
                    
            self.opened_signal.emit()  # 发射串口打开成功的信号
            self.running = True
            
            self.serial.flushInput()  # 清空缓冲区
            
            while self.running:
                # data_in = self.serial.read(self.serial.in_waiting)
                # if data_in:
                #    self.received_signal.emit(data_in)
                data_in = self.serial.readline() 
                if data_in:
                    self.received_signal.emit(data_in)
        except serial.SerialException as e:
            self.error_signal.emit(str(e))  # 发射错误信号
            print(f"无法打开串口: {e}")
            return  # 添加 return 以退出线程
        finally:
            if self.serial and self.serial.isOpen():
                self.serial.close()  # 确保在退出线程前关闭串口

    def stop(self):
        self.running = False
        if self.serial and self.serial.isOpen():
            self.serial.close()

    def write_data(self, data):
        if self.serial and self.serial.isOpen():
            self.serial.write(data)

# 主窗口类
class MainApp(QMainWindow, qt_ui.Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.serial_thread = None  # 添加这行来初始化 serial_thread
        self.checkBox_3.setChecked(True)

        self.serial_port_timer = QTimer(self)
        self.serial_port_timer.timeout.connect(self.populate_serial_ports)
        self.serial_port_timer.start(1000)  # 每1000毫秒（1秒）更新一次

        # 填充可用的串口列表
        self.populate_serial_ports()

        # 连接按钮信号
        self.pushButton.clicked.connect(self.send_data)
        self.pushButton_2.clicked.connect(self.clear_text_edit)
        self.pushButton_3.clicked.connect(self.clear_text_browser)
        self.pushButton_5.clicked.connect(self.close_serial_port)
        self.pushButton_6.clicked.connect(self.open_serial_port)
        
        self.pushButton_5.setEnabled(False)
        # 串口实例
        self.serial = None    
        
    def clear_text_edit(self):
        # 清空 textEdit 的内容
        self.textEdit.clear()

    def clear_text_browser(self):
        # 清空 textBrowser 的内容
        self.textBrowser.clear()

    def handle_serial_error(self, error_message):
        QMessageBox.critical(self, "串口错误", error_message)
        
    def populate_serial_ports(self):
        current_selection = self.comboBox.currentText()  # 保存当前选择
        available_ports = [p.device for p in serial.tools.list_ports.comports()]
        self.comboBox.clear()  # 清空当前列表
        self.comboBox.addItems(available_ports)  # 添加新的可用串口列表

        # 如果之前选择的串口仍然在可用的列表中，重新选择它
        if current_selection in available_ports:
            self.comboBox.setCurrentText(current_selection)

    def open_serial_port(self):
        selected_port = self.comboBox.currentText()
        selected_baudrate = int(self.comboBox_2.currentText())
        selected_databits = int(self.comboBox_3.currentText())
        selected_parity = self.get_parity(self.comboBox_4.currentText())
        selected_stopbits = self.get_stop_bits(self.comboBox_5.currentText())
        dtr_enabled = self.checkBox_3.isChecked()
        rts_enabled = self.checkBox_4.isChecked()

        # 创建新的串口线程
        #self.serial_thread = SerialThread(selected_port, selected_baudrate)
        self.serial_thread = SerialThread(
            port=selected_port,
            baudrate=selected_baudrate,
            databits=selected_databits,
            parity=selected_parity,
            stopbits=selected_stopbits,
            dtr=dtr_enabled,
            rts=rts_enabled
        )
        self.serial_thread.error_signal.connect(self.handle_serial_error)  # 连接错误信号
        self.serial_thread.opened_signal.connect(self.handle_serial_opened)  # 连接成功信号
        self.serial_thread.start()
        self.serial_thread.received_signal.connect(self.on_data_received)

    def handle_serial_error(self, error_message):
        QMessageBox.critical(self, "错误", f"打开串口失败: {error_message}")
        self.serial_thread = None
        #self.radioButton.setChecked(False)


    def handle_serial_opened(self):
        QMessageBox.information(self, "信息", "串口打开成功")
        self.radioButton.setChecked(True)
        self.pushButton_6.setEnabled(False)
        self.pushButton_5.setEnabled(True)

    def get_parity(self, parity_str):
        parity_dict = {
            "None": serial.PARITY_NONE,
            "Odd": serial.PARITY_ODD,
            "Even": serial.PARITY_EVEN,
            "Mark": serial.PARITY_MARK,
            "Space": serial.PARITY_SPACE
        }
        return parity_dict.get(parity_str, serial.PARITY_NONE)  # 默认为无校验
    
    def get_stop_bits(self, stopbits):
        return {
            '1': serial.STOPBITS_ONE,
            '1.5': serial.STOPBITS_ONE_POINT_FIVE,
            '2': serial.STOPBITS_TWO,
        }.get(stopbits, serial.STOPBITS_ONE)  # 默认为 1 个停止位

    def close_serial_port(self):
        if self.serial_thread and self.serial_thread.isRunning():
            # 停止串口线程
            self.serial_thread.serial.flushInput()  # 关闭前清空缓冲区
            self.serial_thread.stop()  # 这应该会关闭串口
            self.serial_thread.wait()  # 等待线程安全退出
            QMessageBox.information(self, "信息", "串口已关闭")
            self.radioButton.setChecked(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(True)

        else:
            QMessageBox.warning(self, "警告", "串口未打开")
            #self.radioButton.setChecked(False)



    def on_data_received(self, data):
        # 在接收文本框中显示数据，忽略无法解码的字符
        # text = data.decode('utf-8', errors='ignore')
        # self.textBrowser.append(text)
        # 检查 checkBox_5 是否被选中
        if self.checkBox_5.isChecked():
            # 获取当前时间
            current_time = datetime.now()
            # 格式化时间字符串
            time_stamp = current_time.strftime("[%H:%M:%S] ") 
        else:
            time_stamp = ""

        # 假设 data 是从串口接收到的原始字节数据
        # 将其解码为字符串
        if self.checkBox_2.isChecked():
            text = ' '.join(f'{byte:02x}' for byte in data)
        else:
            text = data.decode('utf-8', errors='ignore')
            
        # 在文本前添加时间戳
        text_with_timestamp = time_stamp + "GET->"+ text

        # 将带有时间戳的文本添加到文本浏览器控件
        self.textBrowser.append(text_with_timestamp)

    def send_data(self):
        # 首先检查串口线程是否存在并且串口是否打开
        if not (self.serial_thread and self.serial_thread.serial.isOpen()):
            QMessageBox.warning(self, "警告", "串口未打开")
            return

        # 获取文本编辑框的数据
        text = self.textEdit.toPlainText()

        # 检查数据格式并进行相应的处理
        if self.checkBox.isChecked():
            # 用户选择发送十六进制数据
            try:
                # 将十六进制字符串转换为字节
                data = bytes.fromhex(text)
            except ValueError:
                # 如果转换失败，显示错误消息并返回
                QMessageBox.warning(self, "警告", "无效的十六进制数据")
                return
        else:
            # 用户选择发送普通文本
            data = text.encode('utf-8')

        # 发送数据
        self.serial_thread.write_data(data)

        # 检查是否需要添加时间戳
        if self.checkBox_5.isChecked():
            current_time = datetime.now()
            time_stamp = current_time.strftime("[%H:%M:%S] ")
        else:
            time_stamp = ""

        # 将带有时间戳的文本添加到文本浏览器控件
        display_text = text if not self.checkBox.isChecked() else data.hex()
        text_with_timestamp = time_stamp + "SEND->" + display_text
        self.textBrowser.append(text_with_timestamp)

    def closeEvent(self, event):
        # 窗口关闭时确保停止串口线程
        if self.serial_thread and self.serial_thread.isRunning():
            self.serial_thread.stop()
            logging.debug("停止串口线程")
        event.accept()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
