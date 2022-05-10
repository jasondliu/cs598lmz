import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int


def main():
    lib = ctypes.CDLL("./libcomposition_test.so")
    foo = lib.foo
    foo.restype = ctypes.POINTER(S)
    compose = lib.compose
    compose.argtypes = [ctypes.c_void_p, ctypes.c_long, ctypes.c_long, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    if True:
        a = (ctypes.c_long * 4)()
        a[0] = 1
        a[1] = 2
        a[2] = 3
        a[3] = 4
        b = (ctypes.c_long * 4)()
        b[0] = 4
        b[1] = 3
        b[2] = 2
        b[3] = 1
        com_a = (ctypes.c_long * 4)()

