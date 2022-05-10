import socket
import struct
import os
import sys

def send_file(sock, filename):
    if os.path.isfile(filename):
        # 定义文件头信息，包含文件名和文件大小
        file_info = os.path.basename(filename)
        file_info_size = struct.calcsize('128sl')
        # 定义文件头信息，包含文件名和文件大小
        file_info = os.path.basename(filename)
        file_info_size = struct.calcsize('128sl')
        # 定义文件头信息，包含文件名和文件大小
        file_info = os.path.basename(filename)
        file_info_size = struct.calcsize('128sl')
