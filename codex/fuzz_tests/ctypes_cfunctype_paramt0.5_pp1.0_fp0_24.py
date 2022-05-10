import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int)

def func(arg):
    print(arg)

# now we have a function that takes an int and returns nothing
callback = FUNTYPE(func)

# now pass it to the DLL
lib.set_callback(callback)
</code>

