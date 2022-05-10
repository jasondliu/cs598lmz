import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p(b"abc")

class S2(ctypes.Structure):
    _fields_ = [
        ("hello", ctypes.c_char_p(b"world")),
    ]

if __name__ == "__main__":
    import sys
    if sys.platform == "win32":
        print("Windows has a bug in its printf() that makes the output from this program wrong")
    else:
        print(S().x)
        print(S2().hello)
