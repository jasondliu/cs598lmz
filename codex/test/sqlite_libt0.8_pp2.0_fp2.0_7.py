import ctypes
import ctypes.util
import threading
import sqlite3
import time


class gpsd:  # 打开GPSD服务，读取GPS定位信息
    """GPSD client class"""

    def __init__(self):  # 初始化GPSD服务

        self.libgps = ctypes.CDLL(ctypes.util.find_library('gps'))  # 找到libgps.so

        self.libgps.gps_open.restype = ctypes.c_void_p
        self.session = self.libgps.gps_open(None, None)  # 打开GPSD服务

        if not self.session:  # 判断是否打开成功，可以打印GPSD版本信息
            raise Exception("cannot open gpsd session")

        # create a gps data struct and point our data pointer at it
