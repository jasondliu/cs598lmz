import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb?mode=memory&cache=shared', uri=True)

print("\n")

# Initialize ctypes

# TODO: Add error handling in case the library doesn't load
try:
	print("Trying to load audio library... ")
	lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('audio'))
	print("Done loading audio library\n")
except:
	print("Failed to load audio library\n")
	raise

# TODO: Add error handling in case the library is not properly linked
try:
	print("Trying to load convolution library... ")
	convolver = ctypes.cdll.LoadLibrary(ctypes.util.find_library('convolver'))
	print("Done loading convolution library\n")
except:
	print("Failed to load convolution library\n")
	raise

IMPULSE_RESPONSE_LENGTH = 8192
NUM_CHAN = 2

# Setup convolution
IR = ctypes.c_float*
