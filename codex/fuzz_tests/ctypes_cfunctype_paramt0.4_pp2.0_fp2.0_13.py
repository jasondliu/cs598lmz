import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def c_callback(arg):
    print("Python callback called with arg: {0}".format(arg))
    return arg

# Convert the Python callback into a C pointer
c_callback_func = FUNTYPE(c_callback)

# Pass the c_callback_func pointer to C
lib.set_callback(c_callback_func)

# Call the C function which will in turn call the Python callback
lib.execute_callback(1)
