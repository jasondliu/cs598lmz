import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(a, b):
    return a + b

def main():
    lib = ctypes.cdll.LoadLibrary("./libtest.so")
    lib.f.restype = ctypes.c_int
    lib.f.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.g.restype = ctypes.c_int
    lib.g.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.h.restype = ctypes.c_int
    lib.h.argtypes = [ctypes.c_int, ctypes.c_int]

    assert lib.f(1, 2) == f(1, 2)
    assert lib.g(1, 2) == f(1, 2)
    assert lib.h(1, 2) == f(1, 2)

if __name__ == "__main__":
    main()
