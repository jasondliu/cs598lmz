import socket
import sys
import threading
import os
import datetime
import time
import base64
import struct
import json
from mysocket import *
def send_to_client(sock, filepath, filesize, filetype):
    file = open(filepath, 'rb')

    header = {'filetype': filetype, 'filesize': filesize}
    header_bytes = json.dumps(header).encode('utf-8')
    header_len = struct.pack('i', len(header_bytes))
    sock.sendall(header_len)
    sock.sendall(header_bytes)

    chunk_size = 1024
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        sock.sendall(data)
    file.close()

def send_to_client_video(sock, filepath, filesize, filetype):
    file = open(filepath, 'rb')

    header = {'filetype': filetype, 'filesize': filesize}
