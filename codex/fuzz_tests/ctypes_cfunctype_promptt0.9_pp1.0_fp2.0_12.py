import ctypes
# Test ctypes.CFUNCTYPE
TYPES = ['double', 'i', 'd', 'i']

def cfunc(a, b, c, d):
    """cfunc: (a: float, b: float, c: float, d: float) -> float"""
    return float(len(TYPES))

C = ctypes.CFUNCTYPE
CFunc = C(None, *TYPES)(cfunc)
# Test ctypes.POINTER
array = (ctypes.c_float * 3)()
array[0] = 1.0
array[1] = 2.0
array[2] = 3.0
arr_p = ctypes.pointer(array)
# Test ctypes.c_char
letter = ctypes.c_char('x')
# Test ctypes.c_char_p
manytimes = ctypes.c_char_p("hello, " * 1000)
# Test ctypes.c_double
more_than_one = ctypes.c_double(1.414213562373095048801688724209698078569)
# Test
