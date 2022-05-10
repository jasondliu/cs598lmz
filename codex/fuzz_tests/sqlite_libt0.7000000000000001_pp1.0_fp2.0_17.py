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
    _fields_ = [("received_block_cnt", ctypes.c_uint32),
                ("damaged_block_cnt", ctypes.c_uint32),
                ("received_packet_cnt", ctypes.c_uint32),
                ("lost_packet_cnt", ctypes.c_uint32),
                ("tx_restart_cnt", ctypes.c_uint32),
                ("wifi_adapter_cnt", ctypes.c_uint32),
                ("kbitrate", ctypes.c_uint32),
                ("kbitrate_measured", ctypes.c_uint32),
                ("throughput_measured", ctypes.c_uint32),
                ("mode", ctypes.
