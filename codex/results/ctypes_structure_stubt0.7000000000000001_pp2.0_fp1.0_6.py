import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong()
    y = ctypes.c_ulonglong()
S(x=ctypes.c_longlong(1), y=ctypes.c_ulonglong(2)).x

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_longlong),
                ('y', ctypes.c_ulonglong)]
T(x=1, y=2).x

class U(ctypes.Structure):
    _fields_ = [('x', ctypes.c_longlong),
                ('y', ctypes.c_ulonglong)]
U(x=ctypes.c_longlong(1), y=ctypes.c_ulonglong(2)).x

class V(ctypes.Structure):
    _fields_ = [('x', ctypes.c_longlong),
                ('y', ctypes.c_ulonglong)]
V(x=1, y=2).x

class W(ctypes.Structure):
    x = ctypes.c_longlong()
