<h1 align="center">Prozac 💊</h1>

Prozac is an advanced color-based aimbot and triggerbot for Valorant, made for educational purposes.

## 🛠 Requirements

To get started with Prozac, you will need **one** of the following Arduino boards:

- [Arduino Uno R4 Wifi](https://store-usa.arduino.cc/products/uno-r4-wifi?selectedStore=us)
- [Arduino Leonardo](https://store-usa.arduino.cc/products/arduino-leonardo-with-headers?selectedStore=us)
- [Arduino Micro](https://store-usa.arduino.cc/products/arduino-micro?selectedStore=us)

## 🚀 Quick Start Guide

Video tutorial [here](https://youtu.be/wY2qe_QpO2g)

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
1. Download and install [Python 3.8](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe) as it is the most compatible version for Prozac.
2. Install dependencies with `pip install -r requirements.txt`.
3. Edit your [settings](https://github.com/Primoria/Prozac/edit/main/prozac.py#L10-L18) in `prozac.py`.
4. Run `main.py`, ensure that the outline color of the enemies is set to purple.

## ℹ️ Support
Need assistance or have queries? Join our Discord community for real-time support!

[![Discord Banner](https://discordapp.com/api/guilds/1138653980784857159/widget.png?style=banner2)](https://discord.gg/bsNKqvxvE2)

## 🌟 Upcoming Features
- [x] Smooth aiming implemented.
- [x] Triggerbot feature to be added.
- [x] Code optimization.
- [ ] Better color filtering.

Feel free to contribute or suggest new features!
If you find this project useful or interesting, consider giving it a ⭐️ star to help keep the development going!
