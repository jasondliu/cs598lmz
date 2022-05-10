import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print("func called with %d and %d" % (a, b))
    return a + b

# convert python function to c function
cfunc = FUNTYPE(func)

# call c function
print(cfunc(1, 2))

# call python function
print(func(1, 2))

# call c function with python function
print(cfunc(func(1, 2), func(3, 4)))

# call python function with c function
print(func(cfunc(1, 2), cfunc(3, 4)))
</code>

