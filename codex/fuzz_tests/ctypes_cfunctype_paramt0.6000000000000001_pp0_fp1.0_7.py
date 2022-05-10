import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

# this is the function we will wrap
def function():
    print("Hello World!")
    return 1

# convert the function to a type the C library expects
CMPFUNC = FUNTYPE(function)

# call the C library
lib.run(CMPFUNC)
</code>

