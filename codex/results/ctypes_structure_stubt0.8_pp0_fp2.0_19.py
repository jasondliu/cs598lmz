import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

def func(n):
    lib = ctypes.cdll.LoadLibrary("./libnumba_test.so")
    lib.add_one.argtypes = [ctypes.c_int]
    lib.add_one.restype = ctypes.c_int

    lib.add_one_array.argtypes = [ctypes.POINTER(ctypes.c_int)]
    lib.add_one_array.restype = None

    lib.fib.argtypes = [ctypes.c_size_t]
    lib.fib.restype = ctypes.c_size_t

    lib.sum_array.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_size_t]
    lib.sum_array.restype = ctypes.c_int

    lib.summation.argtypes = [ctypes.POINTER(S), ctypes.c_size_t]
    lib.summation.restype = ctypes
