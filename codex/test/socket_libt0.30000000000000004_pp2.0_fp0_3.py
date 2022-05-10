import socket
import threading
import time
import os
import sys
import json

# 定义全局变量
HOST = '127.0.0.1'
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)
FILEINFO_SIZE = struct.calcsize('128sI')

# 定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小

# 定义客户端类
class TftpClient(object):
    def __init__(self, ADDR):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ADDR = ADDR
