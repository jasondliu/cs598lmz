import ctypes
import ctypes.util
import threading
import sqlite3
import os
from datetime import datetime
from time import sleep


# Global variables for the API
_lib = None
_api = None
_db = None
_cursor = None
_scan_flag = False
_scan_thread = None
_scan_lock = threading.Lock()
_scan_callback = None
_scan_callback_args = None
_scan_callback_thread = None
_scan_callback_lock = threading.Lock()
_scan_callback_data = []
_scan_callback_data_lock = threading.Lock()
_scan_callback_data_cond = threading.Condition()

# Constants
BT_ADDR_LEN = 18
BT_NAME_LEN = 248


# Load the API library and get the API function prototypes
def load_api():
    global _lib
    global _api
    global _db
    global _cursor

    # Load the API library
    _lib = ctypes.CDLL(ctypes.util.find_library("ble"))

    # Get the API function prototypes
    _api = API()


