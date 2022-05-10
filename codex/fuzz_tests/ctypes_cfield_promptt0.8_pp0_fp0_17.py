import ctypes
# Test ctypes.CField


class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class T(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('c', ctypes.c_int),
                ('d', ctypes.c_int),
                ('e', S),
                ('f', ctypes.c_int),
                ('g', ctypes.c_int),
               ]

class U(ctypes.Structure):
    _pack_ = 1
    _fields_ = [('c', ctypes.c_int),
                ('d', ctypes.c_int),
                ('e', ctypes.c_int),
                ('f', ctypes.c_int),
                ('g', ctypes.c_int),
               ]

#print T().__sizeof__()
if sizeof(T) != 24 or sizeof(U) != 20:
    raise RuntimeError, "sizeof(T) failed"

class V(ctypes.
