import ctypes
import ctypes.util
import threading
import sqlite3 as lite
import sys
import time

class libVolume(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.__lib = ctypes.util.find_library("pulse")
        self.__pa = ctypes.CDLL(self.__lib)

        self.__pa.pa_volume_perc_to_linear.argtypes = [ctypes.c_int]
        self.__pa.pa_volume_perc_to_linear.restype = ctypes.c_int

        self.__pa.pa_cvolume_set.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_uint, ctypes.c_int]
        self.__pa.pa_cvolume_set.restype = None

    def set_volume(self, new_vol, name = None):
        if not (name):
            name = ctypes.c_char_p("sink_input".encode())

