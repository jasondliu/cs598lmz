import socket
import time
import sys
from PIL import Image
import cv2
import numpy as np
from video_server.decode import *

LOCAL_IP = '0.0.0.0'
LOCAL_PORT = 10791

count = 0
buffer = 1024

# cv2.namedWindow("frame")

def recvall(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data

def connect(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print( 'Socket created')

    s.bind((ip, port))
    print( 'Socket bind complete')
    s.listen(10)
    print( 'Socket now listening')

    return s

def send_image(conn, image):
    #
