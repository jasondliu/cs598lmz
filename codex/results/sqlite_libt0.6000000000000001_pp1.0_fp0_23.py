import ctypes
import ctypes.util
import threading
import sqlite3
import pymysql
import datetime
import sys
import os
import time
import math
import shutil

# 加载libjpeg库
libjpeg = ctypes.cdll.LoadLibrary(ctypes.util.find_library('jpeg'))

# 解码jpeg图像文件
def decode_jpeg(filename, width, height):
    # 创建错误处理对象
    error_mgr = libjpeg.jpeg_std_error()
    libjpeg.jpeg_create_decompress.restype = ctypes.c_void_p
    libjpeg.jpeg_create_decompress.argtypes = [ctypes.c_void_p]
    libjpeg.jpeg_read_header.restype = ctypes.c_int
    libjpeg.jpeg_read_header.argtypes = [ctypes.c_void_p, ctypes.c_int]
    libjpeg
