import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import signal

# Load the lib
lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('pcap'))

# Declare the types for the lib
lib.pcap_lookupdev.restype = ctypes.c_char_p
lib.pcap_lookupdev.argtypes = [ctypes.c_char_p]
lib.pcap_open_live.restype = ctypes.c_void_p
lib.pcap_open_live.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
lib.pcap_next.restype = ctypes.c_char_p
lib.pcap_next.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p)]
lib.pcap_loop.restype = ctypes.c_int
lib.pcap_loop.argtypes = [
