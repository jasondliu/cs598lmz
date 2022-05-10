import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulonglong
    y = ctypes.c_ulonglong
    z = ctypes.c_ulonglong

class T(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_ulonglong),
        ('y', ctypes.c_ulonglong),
        ('z', ctypes.c_ulonglong),
    ]

class U(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_ulonglong),
        ('y', ctypes.c_ulonglong),
        ('z', ctypes.c_ulonglong),
    ]

class V(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_ulonglong),
        ('y', ctypes.c_ulonglong),
        ('z', ctypes.c_ulonglong),
    ]

class W(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_ulonglong),
       
