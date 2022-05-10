import ctypes
import ctypes.util
import threading
import sqlite3
import re
import time
import datetime
import socket

# Compile regex
pattern = re.compile("(\\d+\\.\\d+\\.\\d+\\.\\d+),\\d+,\\d+,(\\d+),([^,]+),([^,]+),([^,]+),([^,]+),([^,]+),([^,]+)")

# Socket for reading from pf_ring
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 1111))

# Load PF_RING
pfring = ctypes.CDLL(ctypes.util.find_library("pfring"))

# Enable dynamic loading of PF_RING functions
pfring.pfring_open.argtypes = [ctypes.c_char_p]
pfring.pfring_open.restype = ctypes.c_void_p
pfring.pfring_set_application_name.argtypes = [ctypes.c
