import socket 
import time
import cv2
import numpy as np
import os
import threading
import datetime
import pickle
import random
import operator

path ="./dataset/"
time_interval = 10
server_ip_port = ('127.0.0.1',8009) #接收端的ip和端口
#server_ip_port = ('10.188.194.142',8009) #接收端的ip和端口

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(server_ip_port)   #连接

camera = cv2.VideoCapture(0)
camera.set(3,1080)
camera.set(4,720)

# Initialize Haar cascade
