import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def main():
    ctypes.cdll.msvcrt.calloc.restype = ctypes.POINTER(S)
    ctypes.cdll.msvcrt.calloc.argtypes = [ctypes.c_size_t, ctypes.c_size_t]

    p = ctypes.cdll.msvcrt.calloc(2, ctypes.sizeof(S))
    assert p.contents.x == 0
    p.contents.x = 13
    assert p.contents.x == 13
    p = ctypes.cdll.msvcrt.realloc(p, ctypes.sizeof(S))
    assert p.contents.x == 13
    p.contents.x = 42
    assert p.contents.x == 42
    ctypes.cdll.msvcrt.free(p)

    p = ctypes.cdll.msvcrt.calloc(2, ctypes.sizeof(S))
    assert p.contents.x == 0
    p
