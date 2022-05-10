import ctypes
# Test ctypes.CField
import ctypes.test.test_cfiled
assert ctypes.CField is ctypes.test.test_cfiled.CField

# Test ctypes.Structure.from_address()
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

# Test ctypes.BigEndianStructure
class X(ctypes.BigEndianStructure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

# Test ctypes.LittleEndianStructure
class X(ctypes.LittleEndianStructure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

# Test ctypes.Union
class X(ctypes.Union):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

# Test ctypes.POINTER
ctypes.POINTER(ctypes.c_int)

# Test ctypes.POINTER(None)

