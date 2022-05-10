import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8()
    _fields_ = [("x", ctypes.c_uint8)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.POINTER(S))]

def main():
    d = D()

    d.a = ctypes.pointer(S())

main()
