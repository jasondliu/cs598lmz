import socket
import sys
import time
import threading
import tkinter as tk
from tkinter import messagebox

# 定义一个类，继承threading.Thread
class ChatClient(threading.Thread):
    def __init__(self, window):
        # threading.Thread.__init__(self)
        super().__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.window = window
        self.stoped = False

    def run(self):
        # 连接服务器
        server_address = (self.window.server_ip.get(), int(self.window.server_port.get()))
        print('connecting to %s port %s' % server_address)
        self.sock.connect(server_address)
        print('connected to %s port %s' % server_address)

        # 发送用户名
