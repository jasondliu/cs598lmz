import socket
import threading
import time
import picamera
from picamera.array import PiRGBArray
import cv2
import numpy as np

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
