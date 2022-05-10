import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    b = ctypes.c_byte()


def main():
    s = S()
    TYPE_SIZE = ctypes.sizeof(s)
