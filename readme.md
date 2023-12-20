# Serial Assistant for PyQt5 / PyQt5 串口助手

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Serial Assistant for PyQt5 is a serial communication application developed based on PyQt5 and PySerial libraries. It allows users to connect to serial ports, receive, and send data. This program is designed to provide a simple and practical serial tool for various serial communication applications.

PyQt5 串口助手是一个基于 PyQt5 和 PySerial 库开发的串口通信应用程序。它允许用户连接到串口、接收和发送数据。本程序旨在提供一个简单而实用的串口工具，适用于多种串口通信应用。

## Directory Structure / 目录结构

The directory structure of project is as follows:

项目的目录结构如下：

```
D:.
├─build
│  └─main
│      └─localpycs
├─dist
└─qt
    └─__pycache__
```

- `build`: Contains compiled files, which may include the program's executable.
- `dist`: Contains the distribution version of the files if you plan to share your program.
- `qt`: Contains files related to PyQt5.

- `build`: 包含编译生成的文件，可能包括程序的可执行文件。
- `dist`: 包含分发版本的文件，如果你打算分享你的程序。
- `qt`: 包含与 PyQt5 相关的文件。

## Instructions / 使用说明

### Installation of Dependencies / 安装依赖

Before running this program, please make sure you have installed the following dependencies:

在运行此程序之前，请确保你已经安装了以下依赖项：

- Python 3.x
- PyQt5
- PySerial

You can use pip to install PyQt5 and PySerial:

你可以使用 pip 来安装 PyQt5 和 PySerial：

```bash
pip install PyQt5 pyserial
```

### Running the Program / 运行程序

To run the program, please follow these steps:

要运行程序，请执行以下步骤：

1. Navigate to the program's root directory in the terminal.
2. Run the following command to start the program:

1. 在终端中导航到程序的根目录。
2. 运行以下命令启动程序：

```bash
python your_program_name.py
```

### Using the Program / 使用程序

The main interface of the program will display a list of serial ports, receiving area, sending area, and some options for configuring and controlling serial communication. Here are some basic usage instructions:

程序的主界面将显示串口列表、接收区、发送区以及一些选项用于配置和控制串口通信。以下是一些基本的使用说明：

1. Open the serial port / 打开串口：
   - Select the serial port and baud rate to connect to.
   - Click the "Open Serial Port" button to establish a serial connection.

   - 选择要连接的串口和波特率。
   - 点击 "打开串口" 按钮以建立串口连接。

2. Close the serial port / 关闭串口：
   - Click the "Close Serial Port" button to disconnect the serial connection.

   - 点击 "关闭串口" 按钮以断开串口连接。

3. Receiving data / 接收数据：
   - The received data will be displayed in the receiving area, where you can choose whether to display timestamps and hexadecimal data.

   - 接收到的数据将显示在接收区，你可以选择是否显示时间戳和十六进制数据。

4. Sending data / 发送数据：
   - Enter the data to be sent, and choose whether it is hexadecimal data.
   - Click the "Send" button to send the data to the serial port.

   - 输入要发送的数据，并选择是否为十六进制数据。
   - 点击 "发送" 按钮以将数据发送到串口。

### Exiting the Program / 退出程序

Closing the main window or pressing the operating system's close button will exit the program. Before exiting, please make sure to close

 the serial connection.

关闭主窗口或按下操作系统的关闭按钮将退出程序。在退出之前，请确保关闭串口连接。

## Unavailable Settings / 暂不可用设置项

Control bits, parity bits, stop bits, flow control, and DTR/RTS settings are currently unavailable, but we plan to add these features in future versions. Please follow the project updates to get the latest features.

控制位、校验位、停止位、流控以及 DTR/RTS 设置项当前不可用，但我们计划在未来的版本中添加这些功能。请关注项目的更新以获取最新功能。

## Packaging the Application / 打包应用程序

Use PyInstaller to package the application into an executable file:

使用 PyInstaller 将应用程序打包为可执行文件：

```bash
pyinstaller --onefile --windowed your_script.py
```

Replace `your_script.py` with the name of your main Python script file.

将 `your_script.py` 替换为您的主 Python 脚本文件的名称。

## Contributions / 贡献

We welcome contributions! Please submit new features, bug fixes, or improvements through pull requests or issues.

我们欢迎贡献！请通过 pull requests 或 issues 提出新功能、bug 修复或改进。

## Version History / 版本历史

- First release (December 20, 2023): Basic serial communication functions.

- 第一版（2023年12月20日）：基本的串口通信功能。

## Author / 作者

- RENBINGCHENG

## License / 许可证

This project is licensed under the MIT License. Please see the  license.md file for more information.

本项目基于 MIT 许可证。请查看license.md文件以获取更多信息。
