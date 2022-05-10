import socket
import sys
import time
import threading
import os
import random
import cv2
import numpy as np
from PIL import Image
import io
import struct
import pickle
import zlib
import base64

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 10000)
        self.sock.connect(self.server_address)
        self.connection = self.sock.makefile('wb')
        self.img_counter = 0
        self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

    def send_img(self):
        # Start a thread that will perform motion detection
        t = threading.Thread(target=self.motion_detect)
        t.daemon = True
        t.start()

        # Start a thread that will send images to the server
        t2 = threading.Thread(target=self.send_images)
