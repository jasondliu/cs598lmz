import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
 
# Source: https://stackoverflow.com/questions/14085135/python-messagebox-tkinter-and-python-3

# 2.
from tkinter import Tk, messagebox
root = Tk()
root.withdraw()
messagebox.showinfo("Title", "Please enter your credentials")

# 3.
from tkinter import *
root = Tk()
root.withdraw()
messagebox.showinfo("Title", "Please enter your credentials")
