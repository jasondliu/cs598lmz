import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

if __name__ == "__main__":
    s = S()
    s.x = 1
    s.y = 2
    s.z = 3
