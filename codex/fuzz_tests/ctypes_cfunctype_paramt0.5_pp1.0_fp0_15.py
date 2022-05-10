import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def pow(x,y):
    return x**y

def pow_c(x,y):
    return ctypes.c_double(x**y)

def pow_c_int(x,y):
    return ctypes.c_int(x**y)

def pow_c_float(x,y):
    return ctypes.c_float(x**y)

def pow_c_long(x,y):
    return ctypes.c_long(x**y)

def pow_c_longlong(x,y):
    return ctypes.c_longlong(x**y)

def pow_c_short(x,y):
    return ctypes.c_short(x**y)

def pow_c_int64(x,y):
    return ctypes.c_int64(x**y)

def pow_c_uint(x,y):
    return ctypes.c_uint(x**y)

def pow_c_ul
