import socket
import sys
import threading
import time
import tkinter
import tkinter.messagebox
import tkinter.scrolledtext

# 创建窗口
window = tkinter.Tk()
window.title('聊天室')
window.geometry('500x500')

# 创建输入框
var_usr_name = tkinter.StringVar()
var_usr_name.set('请输入用户名')
entry_usr_name = tkinter.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=10, y=10, width=150, height=25)

var_usr_pwd = tkinter.StringVar()
entry_usr_pwd = tkinter.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=10, y=50, width=150, height=25)


