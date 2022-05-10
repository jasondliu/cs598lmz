import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("my_callback called with %d" % x)
    return x + 1

my_callback_c = FUNTYPE(my_callback)

# Call the C function
print("Calling C function")
print(my_callback_c(1))
</code>

