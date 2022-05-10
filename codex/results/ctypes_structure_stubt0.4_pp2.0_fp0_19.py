import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    y = ctypes.c_uint8
    z = ctypes.c_uint8
    w = ctypes.c_uint8

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_uint8),
                ("y", ctypes.c_uint8),
                ("z", ctypes.c_uint8),
                ("w", ctypes.c_uint8)]

def main():
    print("S:", ctypes.sizeof(S))
    print("T:", ctypes.sizeof(T))

if __name__ == "__main__":
    main()
