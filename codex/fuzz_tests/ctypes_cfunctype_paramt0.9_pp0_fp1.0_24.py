import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int
)

sum_ints_c = FUNTYPE(("sum_ints", _libsum))
sum_ints_c.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
sum_ints_c.restype = ctypes.c_int

sum_ints_triple_c = FUNTYPE(("sum_ints_triple", _libsum))
sum_ints_triple_c.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
sum_ints_triple_c.restype = ctypes.c_int


def sum_ints_c_wrapper(ptr, arg0, arg1, nargs0, nargs1):
    """
    Call a C function from Julia, signature:
    c_int sum_ints(c_int x, c_int y, c_int z);
    """
   
