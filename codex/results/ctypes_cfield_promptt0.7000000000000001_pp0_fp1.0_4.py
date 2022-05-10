import ctypes
# Test ctypes.CField
class _CStruct(ctypes.Structure):
    _fields_ = [('c', ctypes.c_int),
                ('s', ctypes.c_short),
                ('i', ctypes.c_int),
                ('l', ctypes.c_long),
                ('p', ctypes.c_void_p)]

class _CUnion(ctypes.Union):
    _fields_ = [('c', ctypes.c_int),
                ('s', ctypes.c_short),
                ('i', ctypes.c_int),
                ('l', ctypes.c_long),
                ('p', ctypes.c_void_p)]

class _COther(ctypes.Structure):
    _fields_ = [('c', ctypes.c_int),
                ('f', ctypes.c_float)]

class _COther2(ctypes.Structure):
    _fields_ = [('c', ctypes.c_int),
                ('f', ctypes.c_float),
                ('other', _COther)]

class _
