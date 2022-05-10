import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# Python 3.x
from tkinter import messagebox
messagebox.showinfo("Title", "a Tk MessageBox")

# Python 2.x
import Tkinter
import tkMessageBox
tkMessageBox.showinfo("Title", "a Tk MessageBox")

# Python 2.x
import Tkinter
import tkMessageBox
top = Tkinter.Tk()
def hello():
    tkMessageBox.showinfo("Say Hello", "Hello World")
B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()
top.mainloop()

# Python 3.x
from tkinter import *
import tkinter.messagebox
top = Tk()
def hello():
    tkinter.messagebox.showinfo("Say Hello", "Hello World")
B1 = Button(top, text = "Say Hello", command = hello)
B1.pack()
top.mainloop()

#
