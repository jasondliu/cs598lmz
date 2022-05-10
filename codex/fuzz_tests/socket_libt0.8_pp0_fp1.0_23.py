import socket
import sys
import threading
import time
import tkinter as tk
import tkinter.messagebox
import tkinter.scrolledtext as scrolledtext

root = tk.Tk()
root.title('ChatRoom')
root.geometry('652x532')

message_list=[]

#连接服务器
def connect():
    HOST=ip.get()
    PORT=int(port.get())
    #创建客户端
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    #创建新线程接收消息
    threading.Thread(target=receiveMsg).start()

#接收消息
def receiveMsg():
    while True:
        try:
            s.settimeout(60)
            response=s.recv(1024
