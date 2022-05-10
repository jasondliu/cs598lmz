import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()

def main():
    s = S()
    s.x = 1.0
    s.y = 2.0
    s.z = 3.0
    print s.x, s.y, s.z
    s.x = s.y = s.z = 4.0
    print s.x, s.y, s.z

main()
