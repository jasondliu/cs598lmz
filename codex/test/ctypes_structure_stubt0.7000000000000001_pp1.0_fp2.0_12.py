import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float * 4
    z = ctypes.c_float * 4 * 4

def main():
    s = S()
