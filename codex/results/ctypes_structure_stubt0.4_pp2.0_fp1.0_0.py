import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("x", ctypes.c_int)]

def main():
    s = S()
    print s.x
    s.x = 1
    print s.x

main()
