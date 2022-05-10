import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def add_numbers(a, b):
    return a + b

f = FUNTYPE(add_numbers)
print(f(5.5, 3.5))
