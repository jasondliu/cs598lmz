import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class QT(object):
    def __init__(self):
        self.__qt_lib = None
        self.__qt_lib_path = None
        self.__qt_lib_name = None
        self.__qt_lib_version = None
        self.__qt_lib_version_str = None
        self.__qt_lib_version_str_full = None
        self.__qt_lib_version_str_full_num = None
        self.__qt_lib_version_str_full_num_arr = None
        self.__qt_lib_version_str_full_num_arr_len = None
        self.__qt_lib_version_str_full_num_arr_len_min = None
        self.__qt_lib_version_str_full_num_arr_len_max = None
        self.__qt_lib_version_str_full_num_arr_len_min_max = None
        self.__qt_lib_version_str_full_num_arr_len_min_
