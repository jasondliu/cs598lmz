import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

def main():
    s = S()
    s.x = 1
    s.y = 2
    print(s.x, s.y)

    t = T(1, 2)
    print(t.x, t.y)

if __name__ == "__main__":
    main()
