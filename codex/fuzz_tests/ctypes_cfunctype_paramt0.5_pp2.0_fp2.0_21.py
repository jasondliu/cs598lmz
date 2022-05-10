import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

# C function definition
def func_c(x):
    return sin(x)

# Create ctypes object
func_c_obj = FUNTYPE(func_c)

# Create ctypes object for sin
sin_obj = FUNTYPE(sin)

# Create ctypes object for cos
cos_obj = FUNTYPE(cos)

# Create ctypes object for exp
exp_obj = FUNTYPE(exp)

# Create ctypes object for log
log_obj = FUNTYPE(log)

# Create ctypes object for sqrt
sqrt_obj = FUNTYPE(sqrt)

# Create ctypes object for pow
pow_obj = FUNTYPE(pow)

# Create ctypes object for sinh
sinh_obj = FUNTYPE(sinh)

# Create ctypes object for cosh
cosh_obj = FUNTYPE(cosh)

# Create ctypes object for tanh
tanh_obj = FUNTYPE(tanh)

# Create ctypes object for asinh
asinh_obj = FUNTYPE(asin
