import socket
import threading
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PIL import Image, ImageTk
from socket import *
from threading import Thread
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

from PIL import Image, ImageTk

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 连接客户端
conn, addr = s.accept()

# 创建窗口
root = Tk()
root.title('聊天室')
root.geometry('500x500')

# 创建控件
t = Text(root)
t.pack()

# 创建
