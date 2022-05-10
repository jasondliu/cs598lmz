import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import pyautogui
pyautogui.alert('This displays some text with an OK button.')

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")
</code>

