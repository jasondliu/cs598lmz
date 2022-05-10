import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    print("callback called with %d, %d" % (x, y))
    return x + y

my_callback_c = FUNTYPE(my_callback)

# Call the C function
print(my_dll.my_c_function(my_callback_c))
</code>

