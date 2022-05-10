import socket, sys
import threading
from time import sleep
import struct
import os
import cv2
import pickle
import numpy as np
import datetime
import time
import datetime
import serial
import pynmea2
import math

global_data = []
global_picture = []
global_time = 0
global_picture_time = 0
global_gps = []
global_gps_time = 0
global_speed = 0
global_speed_time = 0
global_log = []

def serial_read():
    global global_speed
    global global_speed_time
    global global_gps
    global global_gps_time
    global global_log
    ser = serial.Serial('/dev/ttyUSB0', 38400)
    print(ser.name)
    print('serial_read')
    port = '/dev/ttyUSB0'
    ser = serial.Serial(port, baudrate=38400)
    while True:
        data = ser.readline()
        if data.find(b'GGA') > 0:
           
