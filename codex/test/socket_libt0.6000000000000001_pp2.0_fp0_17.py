import socket
import threading
import os
import hashlib

# 定义全局变量
HOST = '127.0.0.1'
PORT = 8888
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

# 创建套接字
tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)

# 定义一个类，实现发送文件和接收文件
class File_Transport(object):
    def __init__(self, conn):
        self.conn = conn

    def put(self, *args):
        # 获取文件路径
        file_path = args[1]
        # 获取文件名
