import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(i):
    print "callback called with", i
    return i * 2

my_callback_func = FUNTYPE(my_callback)

# call the function
print "calling the function"
print my_callback_func(5)
</code>

