import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import tkinter as tk
from tkinter import messagebox

messagebox.showinfo("Title", "a Tk MessageBox")

from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()
messagebox.showinfo("Title", "a Tk MessageBox")

from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()
messagebox.showinfo("Title", "a Tk MessageBox")

#!/usr/bin/python

import tkinter
from tkinter import messagebox

top = tkinter.Tk()

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()

#!/usr/bin/python

import t
