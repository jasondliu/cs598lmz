import ctypes
# Test ctypes.CField
class Test:
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int)
    ]

class Test2:
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int, 4),
        ('c', ctypes.c_int),
        ('d', ctypes.c_short, 12)
    ]

class Test3(ctypes.LittleEndianStructure):
    _fields_ = [
        ('a', ctypes.c_ubyte),
        ('b', ctypes.c_short),
        ('c', ctypes.c_int),
        ('d', ctypes.c_longlong)
    ]

class Test4(ctypes.BigEndianStructure):
    _fields_ = [
        ('a', ctypes.c_ubyte),
        ('b', ctypes.c_short),
        ('c', ctypes.c_int),
        ('d', ctypes.c_longlong)

