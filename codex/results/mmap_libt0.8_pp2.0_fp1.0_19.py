import mmap
import time
import socket
import sys
import os
import struct
from struct import *
import cv2
import numpy
import pdb

class obd_capture:
    def __init__(self,ip,port):
        self.clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.clientsocket.connect((ip,port))
        self.clientsocket.settimeout(2)

    def obd_capture_data(self):
        self.clientsocket.send(struct.pack('!I', 1314))
        data_struct = self.clientsocket.recv(struct.calcsize('!I'))
        print(struct.unpack('!I',data_struct))
        data = self.clientsocket.recv(1280*720*3)
        #data = data.fromhex('7E')
        #data = data.fromhex('E8')
        #data = data.fromhex('04')
        #data = data.fromhex('00')
       
