import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
print(fun())

import ctypes
import os
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
# Cast the Python function to a C function
f = FUNTYPE(os.system)
r = f(b"echo hello")
print(r)

# ############################ ctypes: Structure class and functions #####################

# Check the system for 32- or 64-bit architecture
import struct
print( struct.calcsize("P") * 8)

# Set up code for simple data structure; not endian-specific
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_float), ('y', ctypes.c_double)]

# Create a point and set its values
p = POINT(); p.x, p.y = c_float(1.2), c_double(3.4)

# Use the p oint as the input to a C function
c_point = ctypes.byref(p)
print(c_point)
