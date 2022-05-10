import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# add a button
# https://stackoverflow.com/questions/4480075/python-tkinter-yes-no-box
# https://stackoverflow.com/questions/29832075/how-to-make-a-yes-no-box-in-python-tkinter

# add a button
# https://stackoverflow.com/questions/4480075/python-tkinter-yes-no-box
# https://stackoverflow.com/questions/29832075/how-to-make-a-yes-no-box-in-python-tkinter

import tkinter as tk
from tkinter import messagebox

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon
