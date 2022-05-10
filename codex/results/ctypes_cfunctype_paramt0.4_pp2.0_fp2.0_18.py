import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

#
# This is the function we want to call
#
def myfunc(x):
    return x * x

#
# This is the callback function
#
def mycallback(x):
    print "Callback called with", x
    return x * x

#
# This is the function that takes the callback
#
def call_mycallback(x, f):
    print "Calling callback..."
    return f(x)

#
# This is the function that takes the callback
#
def call_mycallback_twice(x, f):
    print "Calling callback..."
    f(x)
    return f(x)

#
# This is the function that takes the callback
#
def call_mycallback_thrice(x, f):
    print "Calling callback..."
    f(x)
    f(x)
    return f(x)

#
# This is the function that takes the callback
#
def call_mycallback_four(x, f):
    print "Calling callback..."
