# Serial Assistant for PyQt5

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Serial Assistant for PyQt5 是一个串口通信应用程序，基于 PyQt5 和 PySerial 库开发。它允许用户连接到串口，接收和发送数据。本程序旨在提供一个简单而实用的串口工具，适用于多种串口通信应用。

## 特性

- 打开和关闭串口
- 设置串口参数（如波特率、数据位等）
- 发送文本或十六进制数据
- 接收并显示串口数据
- 显示发送数据的时间戳

## 目录结构

你的项目的目录结构如下：

```
D:.
├─build
│  └─main
│      └─localpycs
├─dist
└─qt
    └─__pycache__
```

- `build`: 包含编译生成的文件，可能包括程序的可执行文件。
- `dist`: 包含分发版本的文件，如果你打算分享你的程序。
- `qt`: 包含与 PyQt5 相关的文件。

## 使用说明

### 安装依赖

在运行此程序之前，请确保你已经安装了以下依赖项：

- Python 3.x
- PyQt5
- PySerial

你可以使用pip来安装PyQt5和PySerial：

```bash
pip install PyQt5 pyserial
```

### 运行程序

要运行程序，请执行以下步骤：

1. 在终端中导航到程序的根目录。
2. 运行以下命令启动程序：

```bash
python your_program_name.py
```

### 使用程序

程序的主界面将显示串口列表、接收区、发送区以及一些选项用于配置和控制串口通信。以下是一些基本的使用说明：

1. 打开串口：
   - 选择要连接的串口和波特率。
   - 点击 "打开串口" 按钮以建立串口连接。

2. 关闭串口：
   - 点击 "关闭串口" 按钮以断开串口连接。

3. 接收数据：
   - 接收到的数据将显示在接收区，你可以选择是否显示时间戳和十六进制数据。

4. 发送数据：
   - 输入要发送的数据，并选择是否为十六进制数据。
   - 点击 "发送" 按钮以将数据发送到串口。

### 退出程序

关闭主窗口或按下操作系统的关闭按钮将退出程序。在退出之前，请确保关闭串口连接。

## 暂不可用设置项

控制位、校验位、停止位、流控以及DTR/RTS设置项当前不可用，但我们计划在未来的版本中添加这些功能。请关注项目的更新以获取最新功能。

## 打包应用程序

使用 PyInstaller 将应用程序打包为可执行文件：

```bash
pyinstaller --onefile --windowed your_script.py
```

将 `your_script.py` 替换为您的主 Python 脚本文件的名称。

## 贡献

我们欢迎贡献！请通过 pull requests 或 issues 提出新功能、bug 修复或改进。

## 版本历史

- 第一版（2023年12月20日）：基本的串口通信功能。

## 作者

- RENBINGCHENG

## 许可证

本项目基于 MIT 许可证。请查看 [LICENSE]文件以获取更多信息。

