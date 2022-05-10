import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@FUNTYPE
def mul(a, b):
    return a * b

if __name__ == "__main__":
    print mul(2, 3)
