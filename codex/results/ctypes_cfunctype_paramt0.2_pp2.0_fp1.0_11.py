import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback", a, b)
    return a + b

# convert the Python callback into C callback
c_callback = FUNTYPE(my_callback)

# call the C function, which will call the Python callback
lib.call_callback(c_callback)
</code>

