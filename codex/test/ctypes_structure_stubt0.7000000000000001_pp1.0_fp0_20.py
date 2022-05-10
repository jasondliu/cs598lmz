import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def get_p():
    return ctypes.pointer(S())

def main():
    p = get_p()
    assert p

main()
