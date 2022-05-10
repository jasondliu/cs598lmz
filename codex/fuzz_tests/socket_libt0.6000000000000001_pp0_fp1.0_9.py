import socket
import time
import sys
import os
import re
import struct

def get_file_size(file_path):
    file_size = os.path.getsize(file_path)
    return file_size

def get_file_name(file_path):
    file_name = file_path.split('/')[-1]
    return file_name

def send_file_info(sock, file_size, file_name):
    file_info = struct.pack('128sl', file_name, file_size)
    sock.send(file_info)

def send_file_content(sock, file_path):
    f = open(file_path, 'rb')
    data_size = 0
    while True:
        data = f.read(1024)
        if not data:
            break
        data_size += len(data)
        sock.sendall(data)
    print 'send data size: %d' % data_size

def main(argv):
    if len(argv) < 2:
        print
