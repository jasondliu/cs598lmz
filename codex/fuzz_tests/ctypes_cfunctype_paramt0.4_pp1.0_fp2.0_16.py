import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int) # define a type for the callback function

def myfunc(x):
    print "myfunc called with ", x
    return x

myfunc_c = FUNTYPE(myfunc) # wrap the function

libc.qsort(array, len(array), ctypes.sizeof(ctypes.c_int), myfunc_c) # pass the wrapped function
</code>

