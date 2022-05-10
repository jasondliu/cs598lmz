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
        print "Socket Created"

        try:
            self.socket.connect((self.host, self.port))
            print "Socket connected to " + self.host + " on ip " + str(self.port)
        except:
            print "Connection Error"
            sys.exit()

    def send_instruction(self, instruction):
        self.socket.send(instruction)

def main():
    client = Client("192.168.43.141", 1337)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow("frame", frame)
        cv2.waitKey(1)

