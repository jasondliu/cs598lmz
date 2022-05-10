import _struct
import time
import math
import random
import sys
import os
import datetime

#import cv2

#from PIL import Image
#import pytesseract

def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_ts():
    return time.time()

def get_date():
    return datetime.datetime.now().strftime('%Y-%m-%d')

def get_datetime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_microsecond():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

def get_day():
    return datetime.datetime.now().strftime('%Y-%m-%d')

def get_hour():
    return datetime.datetime.now().strftime('%Y-%
