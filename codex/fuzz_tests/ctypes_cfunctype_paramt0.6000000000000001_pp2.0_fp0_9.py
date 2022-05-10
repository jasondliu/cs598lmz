import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def wrapper(f):
    return FUNTYPE(f)

def make_function(n, c_func):
    return Function(n, wrapper(c_func))

f_sin = make_function("f_sin", math.sin)
f_cos = make_function("f_cos", math.cos)
f_tan = make_function("f_tan", math.tan)
f_log = make_function("f_log", math.log)
f_exp = make_function("f_exp", math.exp)
