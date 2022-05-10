import socket
import sys
import time
import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont

# 定义全局变量
HOST = '127.0.0.1'
PORT = 10086
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 创建socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
client_socket.connect(ADDR)

# 创建一个窗口
root = tk.Tk()
root.title('聊天室')
root.geometry('600x500')

# 显示聊天内容的框架
frame_l = tk.Frame(width=500, height=400, b
