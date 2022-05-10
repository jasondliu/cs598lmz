import ctypes
# Test ctypes.CFUNCTYPE()
CFUNCTYPE = ctypes.CFUNCTYPE
c_int = ctypes.c_int
c_void_p = ctypes.c_void_p

# Check signature of no-arg function
def func_noarg():
    return 1

func_noarg_t = CFUNCTYPE(c_int)(func_noarg)
assert func_noarg_t() == 1

# Check signature of one-arg function
def func_witharg(arg):
    return arg

func_witharg_t = CFUNCTYPE(c_void_p, c_void_p)(func_witharg)
assert func_witharg_t(42) == 42

# Check signature of two-arg function
def func_witharg_int(arg1, arg2):
    return arg1 + arg2

func_witharg_int_t = CFUNCTYPE(c_int, c_int, c_int)(func_witharg_int)
assert func_witharg_int_t(40, 2) == 42
