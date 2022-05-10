import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import sys

# from ctypes import *

# Load the shared library into ctypes
lib = ctypes.CDLL(ctypes.util.find_library('c'))

# Set argtypes for the function 'printf'
lib.printf.argtypes = [ctypes.c_char_p]

# Call the function using the ctypes input
lib.printf(b"Hello, World!\n")

# Create a ctypes POINTER for a c_char array

# Create a ctypes c_char array
message = b'Hello, World!'

# Obtain a pointer to the c_char array
lib.printf(message)

# Create a ctypes string
message_string = ctypes.c_char_p(b'Hello, World!')

# Call printf with the ctypes string
lib.printf(message_string)

# Create a ctypes string buffer
message_buffer = ctypes.create_string_buffer(b'Hello, World!')

# Call printf with the ctypes string buffer
lib.printf(message_buffer
