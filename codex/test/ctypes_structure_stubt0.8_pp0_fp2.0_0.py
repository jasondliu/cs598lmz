import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short

class D(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_short),
        ("y", ctypes.c_short),
    ]

def main():
    print(ctypes.sizeof(ctypes.c_short))
    print(ctypes.sizeof(ctypes.c_int))
    print(ctypes.sizeof(ctypes.c_long))
    print(ctypes.sizeof(ctypes.c_longlong))

    print(ctypes.sizeof(S))
    print(ctypes.sizeof(D))

    print(ctypes.align(ctypes.c_short))
    print(ctypes.align(ctypes.c_int))
    print(ctypes.align(ctypes.c_long))
    print(ctypes.align(ctypes.c_longlong))

    print(ctypes.alignment(ctypes.c_short))
