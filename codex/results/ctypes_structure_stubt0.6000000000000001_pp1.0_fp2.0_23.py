import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

if __name__ == '__main__':
    s = S()
    s.x = 42
    s.y = -1
    print 's.x', s.x
    print 's.y', s.y
