import ctypes
# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

# Test ctypes.POINTER
@ctypes.POINTER(ctypes.c_int)
def add(a, b):
    return a + b

# Test ctypes.Structure
@ctypes.Structure
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

# Test ctypes.Union
@ctypes.Union
class Point(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

# Test ctypes.BigEndianStructure
@ctypes.BigEndianStructure
class Point(ctypes.BigEndianStructure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

# Test ctypes.LittleEndianStructure

