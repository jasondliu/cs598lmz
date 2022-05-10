import ctypes
ctypes.cdll.LoadLibrary('libX11.so')
ctypes.cdll.LoadLibrary('libXext.so')
ctypes.cdll.LoadLibrary('libXrender.so')

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import time
import threading
import traceback

def get_current_time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

def get_current_date_str():
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))

def get_current_time_stamp():
    return time.time()

def get_time_stamp(t):
    return time.mktime(time.strptime(t, "%Y-%m-%d %H:%M:%S"))

def get_time_diff_str(start_
