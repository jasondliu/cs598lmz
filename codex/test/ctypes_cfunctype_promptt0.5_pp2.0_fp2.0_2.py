import ctypes
# Test ctypes.CFUNCTYPE
def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a - b

CALLBACK_FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
callback_func = CALLBACK_FUNC(my_callback)

print("Calling callback_func returned %d" % callback_func(3, 2))

# Test ctypes.WINFUNCTYPE
def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a - b

