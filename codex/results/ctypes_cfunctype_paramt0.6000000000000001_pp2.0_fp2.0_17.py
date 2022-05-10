import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float, ctypes.c_int)

# create the function using the ctypes pointer

func = FUNTYPE(lib.poly)

# call the function

print(func(x, n))

# now do the same thing but with a Python function

def poly(x, n):
    p = 1.0
    for i in range(n):
        p *= x
    return p

# convert the Python function to a C function pointer

CMPFUN = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float, ctypes.c_int)
cfunc = CMPFUN(poly)

# call the Python function

print(cfunc(x, n))

# now do the same thing with a wrapper

@CMPFUN
def poly(x, n):
    p = 1.0
    for i in range(n):
        p *= x
    return p

print(poly(x, n))

# and now with an argument checker

