import ctypes
# Test ctypes.CField

if __name__ == "__main__":

    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_ubyte),
                    ("b", ctypes.CField)]

    class Y(ctypes.Union):
        _fields_ = [("a", ctypes.c_ubyte),
                    ("b", ctypes.CField)]

    for cls in X, Y:
        x = cls()
        print(x)
        print("a:", x.a)
        try:
            print("b:", x.b)
        except ValueError as details:
            print("b raises ValueError:", details)
