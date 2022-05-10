import socket
import time
import threading
import sys
import os
import struct

HOST = '127.0.0.1'
PORT = 8888

# 定义文件保存路径
# 获取当前路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 定义文件路径
file_path = os.path.join(BASE_DIR, 'test.txt')

# 定义文件头信息，包含文件名和文件大小
file_info_size = struct.calcsize('128sl')

# 定义接收文件函数
def recv_file(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # 接收客
