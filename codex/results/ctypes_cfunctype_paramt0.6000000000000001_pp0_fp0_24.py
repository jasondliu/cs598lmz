import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_func(a, b):
    def func(x):
        return a + b*x
    return func

# make a C function pointer
func = make_func(2.0, 3.0)
cfunc = FUNTYPE(func)

# call the function pointer
print(cfunc(4.0))
# 14.0
</code>

