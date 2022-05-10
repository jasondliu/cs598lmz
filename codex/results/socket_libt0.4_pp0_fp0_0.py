import socket
import threading
import time
import random
import struct
import sys

# 主要功能：
# 1. 连接服务器，发送消息
# 2. 从服务器接收消息
# 3. 关闭连接

class ChatClient:
    def __init__(self, host='127.0.0.1', port=9999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (host, port)
        self.users = {}
        self.event = threading.Event()

    # 连接服务器
    def connect(self):
        self.sock.connect(self.addr)
        threading.Thread(target=self.recv).start()

    # 断开连接
    def disconnect(self
