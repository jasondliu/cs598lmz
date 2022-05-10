import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# create a callback function with the correct signature
# NOTE: the callback function must have an int return type,
# the number of parameters must be correct, and the parameters
# must have the correct types
def mycallback(x, y):
    print("Python: mycallback", x, y)
    return 42

# convert the Python callback into a C callback
cfunc = FUNTYPE(mycallback)

# now call the C function, which will call the Python callback
print(mycfunc(10, 20, cfunc))
</code>
Prints:
<code>C: mycfunc 10 20
Python: mycallback 10 20
42
</code>

