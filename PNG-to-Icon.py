import os
import sys
from PIL import Image
import tkinter as tk
from tkinter import messagebox

def get_exe_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def popup(msg, title="PNG to ICO"):
    root = tk.Tk()
    root.withdraw()  # 隱藏主視窗
    messagebox.showinfo(title, msg)

def main():
    exe_dir = get_exe_dir()
    png_path = os.path.join(exe_dir, "icon.png")
    ico_path = os.path.join(exe_dir, "icon.ico")

    if not os.path.exists(png_path):
        popup("❌ icon.png 不存在！\n請將 PNG 與此 EXE 放在同一資料夾內")
        return

    try:
        img = Image.open(png_path).convert("RGBA")
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(ico_path, format="ICO", sizes=sizes)
        # popup("✅ 轉檔完成：icon.ico 已成功輸出！")
    except Exception as e:
        popup(f"❌ 發生錯誤：{e}")

if __name__ == '__main__':
    main()
