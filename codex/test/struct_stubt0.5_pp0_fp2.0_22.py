from _struct import Struct
s = Struct.__new__(Struct)
s.size = 1
s.format = 'x'
s.unpack = Struct.unpack
s.pack = Struct.pack

# Create a ctypes pointer to a function
from ctypes import *
c_func = CFUNCTYPE(c_int, c_int, c_int)
c_func.restype = c_int

# Create a ctypes pointer to a function that returns a pointer
from ctypes import *
c_func = CFUNCTYPE(POINTER(c_int))
c_func.restype = POINTER(c_int)

# Create a ctypes pointer to a function that returns a pointer to a function
from ctypes import *
c_func = CFUNCTYPE(CFUNCTYPE(c_int, c_int))
c_func.restype = CFUNCTYPE(c_int, c_int)

# Create a ctypes pointer to a function that returns a pointer to a function that returns a pointer
