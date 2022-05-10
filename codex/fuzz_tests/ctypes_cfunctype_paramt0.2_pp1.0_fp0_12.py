import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def c_callback(arg):
    print "C callback called with arg:", arg
    return arg

c_callback_func = FUNTYPE(c_callback)

# This is the function that will be called from C
def py_callback(arg):
    print "Python callback called with arg:", arg
    return arg

# This is the function that will be called from C
def py_callback2(arg):
    print "Python callback2 called with arg:", arg
    return arg

# This is the function that will be called from C
def py_callback3(arg):
    print "Python callback3 called with arg:", arg
    return arg

# This is the function that will be called from C
def py_callback4(arg):
    print "Python callback4 called with arg:", arg
    return arg

# This is the function that will be called from C
def py_callback5(arg):
    print "Python callback5 called with arg:", arg
    return arg

# This is the function that
