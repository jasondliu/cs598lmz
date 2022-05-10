import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define callback function
def myfunc(i):
    print "called back with", i
    return i*2

# convert function to CFUNCTYPE
cfunc = FUNTYPE(myfunc)

# call function
print cfunc(3)
