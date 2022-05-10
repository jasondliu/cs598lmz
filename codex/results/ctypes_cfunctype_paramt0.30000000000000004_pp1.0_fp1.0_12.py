import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def f(x):
    return x**2

def f_double(x):
    return 2*x

def f_int(x):
    return 2

def f_int_double(x):
    return 2.0

def f_double_int(x):
    return 2

def f_double_double(x):
    return 2.0

def f_int_int(x):
    return 2

def f_int_int_int(x):
    return 2

def f_int_int_double(x):
    return 2.0

def f_int_double_int(x):
    return 2

def f_int_double_double(x):
    return 2.0

def f_double_int_int(x):
    return 2

def f_double_int_double(x):
    return 2.0

def f_double_double_int(x):
    return 2

def f_double_double_double(
