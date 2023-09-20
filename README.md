<h1 align="center">Prozac 💊</h1>

A Python-based educational project for real-time color-based object tracking using computer vision, integrated with Arduino for enhanced security features.
</p>

![326271580_829989831434355_6228617060849086479_n](https://github.com/Primoria/Prozac/assets/137751691/dc993b97-1e92-44e4-9e46-ce24c71c9a8e)


## 🛠 Requirements

To get started with Prozac, you will need **one** of the following Arduino boards:

- [Arduino Uno R4 Wifi](https://store-usa.arduino.cc/products/uno-r4-wifi?selectedStore=us)
- [Arduino Leonardo](https://store-usa.arduino.cc/products/arduino-leonardo-with-headers?selectedStore=us)
- [Arduino Micro](https://store-usa.arduino.cc/products/arduino-micro?selectedStore=us)

## 🚀 Quick Start Guide

### Step 1: Configure Arduino as Mouse
1. Download and install the [Legacy Arduino IDE](https://downloads.arduino.cc/arduino-1.8.19-windows.exe).
2. Navigate to your Arduino IDE's `board.txt` file, usually located in `C:\Program Files (x86)\Arduino\hardware\arduino\avr`.
3. Locate the section specific to your Arduino board (e.g., Leonardo or Micro).
4. Update the `vid` and `pid` values to match those of your mouse. To find these values, Check the [FAQ](https://github.com/Primoria/Prozac/wiki#faq).
5. Save changes and close the file.

> [!NOTE]  
> The above configure method doesn't apply to Arduino Uno R4 Wifi. Please consult the Discord server for guidance.

### Step 2: Upload Mouse Sketch
1. Open `mouse.ino` from the downloaded repository's `mouse` folder.
2. Select your Arduino board and port in the Arduino IDE.
3. Upload the sketch.
4. Confirm your Arduino is recognized as a HID device with your mouse's `vid` and `pid`.

### Step 3: Run Python Script
1. Download and install the [latest Python version](https://www.python.org/downloads/).
2. Install dependencies with `pip install -r requirements.txt`.
3. Edit your [settings](https://github.com/Primoria/Prozac/blob/main/prozac.py#L10-L20) in `prozac.py`.
4. Run `main.py`.

## ℹ️ Support
Need assistance or have queries? Join our Discord community for real-time support!

[![Discord Banner](https://discordapp.com/api/guilds/1138653980784857159/widget.png?style=banner2)](https://discord.gg/bsNKqvxvE2)

## 🌟 Upcoming Features
- [x] Smooth aiming implemented.
- [ ] GUI development in progress.
- [ ] Triggerbot feature to be added.
- [ ] Code optimization.

Feel free to contribute or suggest new features!
If you find this project useful or interesting, consider giving it a ⭐️ star to help keep the development going!
