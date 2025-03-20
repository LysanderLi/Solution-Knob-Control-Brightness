# QuecPython 旋钮控灯方案

中文 | [English](README.MD)

欢迎来到 QuecPython 旋钮控灯方案仓库！本仓库提供了一个全面的解决方案，用于使用 QuecPython 实现旋钮控灯。

## 目录

- [介绍](#介绍)
- [功能](#功能)
- [快速开始](#快速开始)
  - [先决条件](#先决条件)
  - [安装](#安装)
  - [运行应用程序](#运行应用程序)
- [目录结构](#目录结构)
- [使用](#使用)
- [贡献](#贡献)
- [许可证](#许可证)
- [支持](#支持)

## 介绍

QuecPython 推出了针对PWM调光的解决方案，包括PWM循环呼吸灯，旋钮控制等。

通过调用QuecPython封装的接口，仅需使用几行代码就可以是PWM控灯的效果，搭配上一些其他的设备，实现设备控制灯光亮度，如使用ADC采集旋钮的电压值，来按比例改变PWM的占空比，进而实现旋钮控制灯光亮度。

## 功能

- **循环呼吸灯**：LED灯逐渐变亮，再逐渐变暗
- **旋钮控制**：通过旋转旋钮改变LED灯亮度

## 快速开始

### 先决条件

在开始之前，请确保您具备以下先决条件：

- **硬件**：
  - 一块能使用GPIO，PWM和ADC的QuecPython开发板
  - USB 数据线（USB-A 转 USB-C）
  - 电脑（Windows 7、Windows 10 或 Windows 11）
- **软件**：
  - QuecPython 模块的 USB 驱动
  - QPYcom 调试工具
  - QuecPython 固件及相关软件资源
  - Python 文本编辑器（例如，[VSCode](https://code.visualstudio.com/)、[Pycharm](https://www.jetbrains.com/pycharm/download/)）

### 安装

1. **克隆仓库**：
   ```bash
   git clone https://github.com/QuecPython/solution-Knob-Control-Brightness
   cd solution-Knob-Control-Brightness
   ```

2. **烧录固件**：

   按照[说明](https://python.quectel.com/doc/Application_guide/zh/dev-tools/QPYcom/qpycom-dw.html#Download-Firmware)将固件烧录到开发板上。

### 运行应用程序

1. **连接硬件**：
   - 使用 USB 数据线将开发板连接到计算机的 USB 端口。

2. **将代码下载到设备**：
   - 启动 QPYcom 调试工具。
   - 将数据线连接到计算机。
   - 按下开发板上的 **PWRKEY** 按钮启动设备。
   - 按照[说明](https://python.quectel.com/doc/Application_guide/zh/dev-tools/QPYcom/qpycom-dw.html#Download-Script)将 `code` 文件夹中的`demo.py`文件导入到模块的文件系统中，保留目录结构。

3. **运行应用程序**：
   - 选择 `File` 选项卡。
   - 选择 `demo.py` 脚本。
   - 右键单击并选择 `Run` 或使用`运行`快捷按钮执行脚本。

## 目录结构

```plaintext
solution-Knob-Control-Brightness/
├── code/
│   ├── demo.py        		# 执行脚本
├── LICENSE					#许可证
├── READMEZH.md             # 本 README 文件
└── README.md				# README 英文文件
```

## 使用

点击[这里](https://python.quectel.com/doc/Application_guide/zh/solutions/Wear/index.html)查看可穿戴解决方案的详细实现。

## 贡献

我们欢迎对本项目的改进做出贡献！请按照以下步骤进行贡献：

1. Fork 此仓库。
2. 创建一个新分支（`git checkout -b feature/your-feature`）。
3. 提交您的更改（`git commit -m 'Add your feature'`）。
4. 推送到分支（`git push origin feature/your-feature`）。
5. 打开一个 Pull Request。

## 许可证

本项目使用 Apache 许可证。详细信息请参阅 [LICENSE](LICENSE) 文件。

## 支持

如果您有任何问题或需要支持，请参阅 [QuecPython 文档](https://python.quectel.com/doc) 或在本仓库中打开一个 issue。
