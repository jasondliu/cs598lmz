import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def function(x, y):
    return x + y

# make a copy of the function, and make it into a CFUNCTYPE
f = FUNTYPE(function)

# call the function through the CFUNCTYPE
print(f(1, 2))

# now make a new function that uses the same address as f
f2 = FUNTYPE(f)
print(f2(3, 4))
</code>

