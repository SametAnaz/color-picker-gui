import pyautogui
from PIL import Image, ImageTk
import tkinter as tk
import subprocess
import os

screenshot_path = "/tmp/screen_capture.png"

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)

def copy_color_at(x, y):
    img = Image.open(screenshot_path)
    rgb = img.getpixel((x, y))
    hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb).upper()
    subprocess.run(['xclip', '-selection', 'clipboard'], input=hex_color.encode())
    subprocess.run(['notify-send', hex_color])
    print(f"[+] Copied color at ({x}, {y}): {hex_color}")

def on_click(event, window):
    x, y = event.x, event.y
    copy_color_at(x, y)
    window.destroy()
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

def show_image_and_listen():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)

    img = Image.open(screenshot_path)
    tk_img = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(root, width=img.width, height=img.height)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
    canvas.bind("<Button-1>", lambda e: on_click(e, root))

    print("[*] Click anywhere on the screenshot to pick a color...")
    root.mainloop()

if __name__ == "__main__":
    os.system("xsetroot -cursor_name crosshair")
    take_screenshot()
    show_image_and_listen()
    os.system("xsetroot -cursor_name left_ptr")
