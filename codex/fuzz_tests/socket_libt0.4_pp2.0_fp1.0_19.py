import socket
import sys
import time
import threading
import random
import json
import os
import getpass
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

# 定义全局变量
HOST = '127.0.0.1'
PORT = 50007
BUFSIZE = 1024
ADDR = (HOST, PORT)

# 定义用户名
username = ''

# 定义窗口
root = tk.Tk()
root.title('聊天室')
root.geometry('500x500')

# 定义输入框
var = tk.StringVar()
var.set('')
e = tk.Entry(root, textvariable=var)
e.place(x=5, y=5, width=300, height=20)

# 定义聊天记录
t = tk.Text
