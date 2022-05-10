import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print "callback called with", x
    return x + 1

callback = FUNTYPE(my_callback)

# call the function
print "calling function"
print lib.my_function(callback)
