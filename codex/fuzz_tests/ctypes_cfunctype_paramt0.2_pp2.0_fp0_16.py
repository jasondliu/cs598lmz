import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

my_callback_c = FUNTYPE(my_callback)

lib.my_function.argtypes = [FUNTYPE]
lib.my_function(my_callback_c)

# Output:
# my_callback called with 1 and 2
# 3
</code>

