# Wearable Solution for QuecPython

[中文](README_ZH.MD) | English

Welcome to the QuecPython Knob Light Solution warehouse! This repository provides a comprehensive solution for implementing knob controlled lights using QuecPython.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Directory Structure](#directory-structure)
- [Contribution](#contribution)
- [License](#license)
- [Support](#support)

## Introduction

QuecPython has launched a solution for PWM dimming, including PWM loop breathing lights and knob control, etc. By calling the interfaces encapsulated by QuecPython, the effect of PWM light control can be achieved with just a few lines of code. Combined with other devices, it can realize the control of light brightness by the device. For example, by using ADC to collect the voltage value of the knob, the duty cycle of PWM can be changed proportionally to achieve the control of light brightness by the knob.

## Features

- **Cycle breathing light** : LED light gradually brightens, then gradually dimmed
- **Knob Control**  : Change the LED light by turning the knob

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites:

- **Hardware**:
  - A QuecPython development board
  - USB Data Cable (USB-A to USB-C)
  - PC (Windows 7, Windows 10, or Windows 11)

- **Software**:
  - USB driver for the QuecPython module
  - QPYcom debugging tool
  - QuecPython firmware and related software resources
  - Python text editor (e.g., [VSCode](https://code.visualstudio.com/), [Pycharm](https://www.jetbrains.com/pycharm/download/))

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/QuecPython/solution-Knob-Control-Brightness
   cd solution-Knob-Control-Brightness
   ```

2. **Flash the Firmware**:

   Follow the [instructions](https://python.quectel.com/doc/Application_guide/en/dev-tools/QPYcom/qpycom-dw.html#Download-Firmware) to flash the firmware to the development board.

### Running the Application

1. **Connect the Hardware**:
   - Insert the SIM card into the SIM card slot.
   - Connect the antenna.
   - Use a USB data cable to connect the development board to the computer's USB port.

2. **Download Code to the Device**:
   - Launch the QPYcom debugging tool.
   - Connect the data cable to the computer.
   - Press the **PWRKEY** button on the development board to start the device.
   - Follow the [instructions](https://python.quectel.com/doc/Application_guide/en/dev-tools/QPYcom/qpycom-dw.html#Download-Script) to import all files within the `code` folder into the module's file system, preserving the directory structure.

3. **Run the Application**:
   - Select the `File` tab.
   - Select the `demo.py` script.
   - Right-click and select `Run` or use the run shortcut button to execute the script.

## Directory Structure

```plaintext
solution-Knob-Control-Brightness/
├── code/
│   ├── demo.py        		# Run Script
├── LICENSE					#license file 
├── READMEZH.md            
└── README.md				
```


## Contribution

We welcome contributions to improve this project! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need support, please refer to the [QuecPython documentation](https://python.quectel.com/doc/en) or open an issue in this repository.