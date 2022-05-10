import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    print("my_callback called with %d and %d" % (x, y))
    return x + y

my_callback_c = FUNTYPE(my_callback)

# Now we can pass my_callback_c to a C function that takes a
# function pointer as an argument.

# This is the C function we are going to call.
# It takes a function pointer as its first argument.
_cfunc = ctypes.CDLL(None).cfunc
_cfunc.argtypes = (FUNTYPE, ctypes.c_int, ctypes.c_int)
_cfunc.restype = ctypes.c_int

# Call the C function.
result = _cfunc(my_callback_c, 1, 2)
print("cfunc returned %d" % result)
</code>

