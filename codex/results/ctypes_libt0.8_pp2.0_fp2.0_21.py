import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.withdraw()

messagebox.showinfo("Title", "MESSAGE TEXT")
