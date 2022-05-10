import ctypes
import ctypes.util
import threading
import sqlite3
import time
from pyftdi.ftdi import Ftdi

# This is the name of a C library that contains the FTDI functions.
# The name of the library varies according to OS, so we use the
# ctypes.util.find_library() function to find the name of the library
# and ctypes.cdll.LoadLibrary() to get the library handle.
libftdi1 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('libftdi1'))

# The following lines set up the return types for the functions we
# will be using.  The entry in the table for each function is a
# tuple with the following elements:
#   - The name of the function as it appears in C code.
#   - The return type of the function.
#   - A tuple containing the types of the parameters to the function.
#
# For each function, the tuple is followed by a line that defines the
# function prototype.  The first parameter in the prototype is a
# handle to the library.  The second parameter is a byte string
# containing the name of the function.
