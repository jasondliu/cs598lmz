import ctypes
# Test ctypes.CFUNCTYPE
def c_callback(c_int, c_int):
    print("c_callback called")
    return c_int * 2

CMPFUNC = ctypes.CFUNCTYPE(c_int, c_int, c_int)

c_callback_func = CMPFUNC(c_callback)
print(c_callback_func(2, 3))

# Test ctypes.WINFUNCTYPE
def w_callback(c_int, c_int):
    print("w_callback called")
    return c_int * 2

CMPFUNC = ctypes.WINFUNCTYPE(c_int, c_int, c_int)

w_callback_func = CMPFUNC(w_callback)
print(w_callback_func(2, 3))

# Test ctypes.PYFUNCTYPE
def py_callback(c_int, c_int):
    print("py_callback called")
    return c_int * 2

CMPFUNC = ctypes.PYFUNCTYPE(c_int,
