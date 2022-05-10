import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def c_callback(f):
    c_f = FUNTYPE(f)
    return c_f

def c_sin(x):
    return math.sin(x)

c_sin_callback = c_callback(c_sin)

def c_cos(x):
    return math.cos(x)

c_cos_callback = c_callback(c_cos)

def c_tan(x):
    return math.tan(x)

c_tan_callback = c_callback(c_tan)

def c_e(x):
    return math.e**x

c_e_callback = c_callback(c_e)

def c_ln(x):
    return math.log(x)

c_ln_callback = c_callback(c_ln)

def c_log(x):
    return math.log10(x)

c_log_callback = c_callback(c_log)

def c_exp(x):
   
