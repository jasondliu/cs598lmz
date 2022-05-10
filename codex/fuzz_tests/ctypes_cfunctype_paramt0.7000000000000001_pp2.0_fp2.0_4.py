import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def py_func(x, y):
    return x + y
py_func_ptr = FUNTYPE(py_func)

# call native function
@native_function(lib, ret=c_int, args=[c_int, c_int])
def native_func(x, y):
    pass

# call python function through native function
@native_function(lib, ret=c_int, args=[c_int, c_int])
def native_func_py(x, y):
    return py_func_ptr(x, y)

# call c function with python function pointer
@native_function(lib, ret=c_int, args=[FUNTYPE, c_int, c_int])
def c_func(func, x, y):
    return func(x, y)

# call python function through c function
@native_function(lib, ret=c_int, args=[c_int, c_int])
def c_func_py(x, y):
