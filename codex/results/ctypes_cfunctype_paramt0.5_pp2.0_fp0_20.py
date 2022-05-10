import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

# Make a function pointer out of it
callback_func = FUNTYPE(callback)

# Make a python callable object
def callable():
    return callback_func()

# Call it
callable()
</code>

