import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time

logfile = "log.txt"

try:
	os.remove(logfile)
except OSError:
	pass

logging.basicConfig(filename=logfile,format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

logging.info("start logging")

#load library
lib = ctypes.cdll.LoadLibrary('./libpycall.dylib')

#Some data need to be packed into a buffer before passing it to C code
class stru_msg_header(ctypes.Structure):
   _pack_=1
   _fields_ = [
       ("len", ctypes.c_long),
       ("type", ctypes.c_char),
       ("subtype", ctypes.c_char*7)
   ]
class stru_msg_body(ctypes.Structure):
    _pack_=1
    _fields_ = [
        ('number',ctypes.c_char*21),
        ('status',ctypes.
