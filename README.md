# Color Picker GUI 🎨

A minimal GUI-based color picker tool for Linux desktops.  
Click anywhere on the screen to select a pixel — the script will copy the pixel's HEX color code to your clipboard and display a desktop notification.
---
! Only for X11 sessions 
---

## ✨ Features

- Crosshair-style cursor during selection  
- Takes fullscreen screenshot to prevent UI interference  
- Click-to-copy selected pixel color (in HEX)  
- GNOME desktop notification with color info  
- Script exits automatically after selection  
- Safe to use — no unintended UI clicks  

---

# ⚙️ Requirements

Tested on **Ubuntu 24.04 LTS (GNOME + X11)**

## 📦 System Dependencies

Install the following system packages:

```bash
sudo apt update
sudo apt install python3-tk libnotify-bin xclip -y
```
## 🐍 Python Dependencies
It is recommended to use a virtual environment:

```bash
python3 -m venv ~/.venvs/colorpicker
source ~/.venvs/colorpicker/bin/activate
pip install pillow pyautogui
```
-pillow: for image processing

-pyautogui: for taking screenshots and getting cursor position

# 🚀 Usage
```bash
run_color_picker.sh
```
The screen will dim (screenshot), and your mouse cursor will change to a crosshair.
Click anywhere to select a color. It will be copied as HEX to your clipboard, and you'll see a desktop notification.

# 📁 Files
`color_picker.py` → Main script

`run_color_picker.sh` → Shell script that activates venv and runs the script

