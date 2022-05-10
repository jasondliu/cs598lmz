import threading
threading.stack_size(20000000)
import os
import sys
import time
import math
import numpy as np
from numpy import NaN, Inf, arange, isscalar, asarray, array
import matplotlib.pyplot as plt
import subprocess
import serial
import opendbpy


global ser 
ser = serial.Serial('COM7',9600)


a=1
while a==1:
    scheck = ser.read()
    try:
        scheck=int(scheck)
        if scheck==0x0D:
            print("Error!!!")
            a=0
            ser.close()
        if scheck==0x01:
            print("Stimulating...")
            a=1
        time.sleep(0.01)
    except:
        time.sleep(0.01)
