import ctypes
# Test ctypes.CFUNCTYPE
def func(arg):
    print "hello", arg

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print cmp_func(42)

# Test ctypes.PYFUNCTYPE
def py_func(arg):
    print "hello", arg
    return arg + 1

PYFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)

py_func = PYFUNC(py_func)

print py_func(42)

# Test ctypes.WINFUNCTYPE
def win_func(arg):
    print "hello", arg
    return arg + 1

WINFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)

win_func = WINFUNC(win_func)

print win_func(42)

# Test ctypes.CFUNCTYPE(None,
