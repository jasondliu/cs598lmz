import ctypes
import ctypes.util
import threading
import sqlite3
import struct
import json
import time

try:
    import gtk
except:
    print("install gtk")
    print("sudo apt-get install python-gtk2")
    exit(0)

class wifibroadcast_rx_status_t(ctypes.Structure):
    _pack_ = 1
