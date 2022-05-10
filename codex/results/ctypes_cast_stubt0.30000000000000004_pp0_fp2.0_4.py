import ctypes
ctypes.cast(ctypes.pointer(ctypes.c_int(0)), ctypes.POINTER(ctypes.c_int))

# examples/python/test_struct.py
import ctypes
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT(10, 20)
print(p.x, p.y)

# examples/python/test_struct.py
import ctypes
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT(10, 20)
print(p.x, p.y)
p.x = 30
print(p.x, p.y)

# examples/python/test_struct.py
import ctypes
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int
