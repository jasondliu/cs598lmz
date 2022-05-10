import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

import tkinter
from tkinter import *
from PIL import ImageTk,Image
import pymysql
import tkinter.messagebox
def login():
    global root
    root = tkinter.Tk()
    root.title('聊天登录')
    root.geometry('600x400+500+200')
    root.resizable(False, False)
    img = Image.open("login.jpg")
    photo = ImageTk.PhotoImage(img)
    lblImage = Label(root, image=photo)
    lblImage.grid(row=0, column=0, columnspan=3, rowspan=5)

    var_usr_name = StringVar()
    var_usr_name.set('example@python.com')
    entry_usr_name = Entry(root, textvariable=var_usr_name)
    entry_usr_name.grid(row=1, column=2, padx
