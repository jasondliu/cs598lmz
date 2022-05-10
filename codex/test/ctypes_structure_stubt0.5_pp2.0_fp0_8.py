import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32
    z = ctypes.c_uint32

class T(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32
    z = ctypes.c_uint32

class U(ctypes.Union):
    _fields_ = [("s", S), ("t", T)]

def main():
    u = U()
    u.s.x = 1
    u.s.y = 2
    u.s.z = 3
