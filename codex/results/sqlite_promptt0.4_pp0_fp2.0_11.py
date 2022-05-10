import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# Load the library
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

# Define the database type
class database(ctypes.Structure):
    pass

# Define the database type pointer
database_p = ctypes.POINTER(database)

# Define the callback function type
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_char_p))

# Define the error handler type
ERROR_HANDLER = ctypes.CFUNCTYPE(None, database_p, ctypes.c_int, ctypes.c_char_p)

# Create the callback function
def callback(data, argc, argv, azColName):
    print("Callback data: {}".format(data))
    print("Callback argc: {}".format(argc))
    print("Callback
