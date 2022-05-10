import ctypes
import ctypes.util
import threading
import sqlite3
import logging

# Initialize logging
logging.basicConfig(filename='example.log',
					level=logging.DEBUG,
					format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# Find the .so file with ctypes.util.find_library
# and load it with ctypes.cdll.LoadLibrary
_file = 'libmongoose.so'
_path = '/home/pi/dev/EmbeddedSystems/WebServer/c/'
_name = 'mongoose'

try:
	lib = ctypes.cdll.LoadLibrary(_path + _file)
except OSError:
	logging.error("Could not load library {0}".format(_file))
	raise

# Set the return type and argument types of the functions
lib.mg_start.restype = ctypes.c_void_p
