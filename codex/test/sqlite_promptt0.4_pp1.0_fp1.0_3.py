import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/Documents/nfc_tag_reader/rfid.db")
# Test sqlite3.connect("C:\\Users\\Kris\\Documents\\GitHub\\nfc_tag_reader\\rfid.db")

#
#
#

# Load the shared library into ctypes
nfc = ctypes.CDLL(ctypes.util.find_library('nfc'))

# Define ctypes prototypes for the functions we are going to call
nfc.nfc_init.argtypes = (ctypes.POINTER(ctypes.c_void_p),)
nfc.nfc_init.restype = ctypes.c_int
nfc.nfc_open.argtypes = (ctypes.c_void_p,)
nfc.nfc_open.restype = ctypes.c_void_p
nfc.nfc_initiator_init.argtypes = (ctypes.c_void_p,)
nfc.nfc_initiator_init.restype = ctypes.c_int
nfc.nfc_
