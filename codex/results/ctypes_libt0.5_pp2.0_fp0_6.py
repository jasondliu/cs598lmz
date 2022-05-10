import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
import numpy as np
import os, sys, time
import cv2
import serial
import serial.tools.list_ports
import threading
import winsound

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

# Set up the serial port
print('Waiting for serial port to be connected...')
while True:
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'USB-SERIAL CH340' in p[1]:
            print('Found serial port: ' + p[0])
            ser = serial.Serial(p[0], 115200)
            break
    if ser.is_open:
        break
    time.sleep(1)

# Set up the plot
win = pg.GraphicsWindow(title="Real-time plot")
win.resize(1000,600)
win.setWindowTitle('Real-
