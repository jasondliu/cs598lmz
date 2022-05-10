import ctypes
# Test ctypes.CField.bitsize
import _ctypes

class Packed1(ctypes.Structure):
    _fields_ = [("f", ctypes.c_int, 1)]

class Packed2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int, 1),
                ("b", ctypes.c_int, 1)]

class Packed3(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int, 1),
                ("b", ctypes.c_int, 1),
                ("c", ctypes.c_int, 1)]

if __name__ == "__main__":
    import sys

    print(Packed3._pack_)
    for t in [Packed1, Packed2, Packed3]:
        for i in range(sys.getcheckinterval()):
            # force garbage collection
            t()
        print(t._pack_)
