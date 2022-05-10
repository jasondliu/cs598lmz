import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# function to be called
def myfunc(x):
    return x + 1

# create a function pointer
f = FUNTYPE(myfunc)

# call the function pointer
print(f(1))
</code>

