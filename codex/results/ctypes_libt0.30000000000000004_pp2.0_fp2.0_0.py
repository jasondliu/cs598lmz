import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#import tkinter as tk
#from tkinter import messagebox
#root = tk.Tk()
#root.withdraw()
#messagebox.showinfo("Title", "a Tk MessageBox")

import os
os.system("msg * You've got mail!")

import subprocess
subprocess.Popen(['start', 'msg', '*', 'You have got mail!'], shell=True)

import win32api
win32api.MessageBox(0, 'Your text', 'Your title')

import win32gui
win32gui.MessageBox(0, 'Your text', 'Your title')

import win32ui
win32ui.MessageBox("Your text", "Your title")

import win32con
win32con.MB_OK
win32con.MB_OKCANCEL
win32con.MB_ABORTRETRYIGNORE
win32con.MB_YESNOCANCEL
win32con.MB_YESNO
win32
