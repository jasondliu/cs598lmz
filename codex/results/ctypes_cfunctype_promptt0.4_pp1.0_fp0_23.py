import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    print "func", a, b

def func_with_errcheck(a, b):
    print "func_with_errcheck", a, b
    return a

def errcheck(result, func, args):
    print "errcheck", result, func, args
    return result

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
CALLBACK_WITH_ERRCHECK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, errcheck=errcheck)

callback = CALLBACK(func)
callback(1, 2)

callback = CALLBACK(func_with_errcheck)
callback(1, 2)

callback = CALLBACK_WITH_ERRCHECK(func)
callback(1, 2)

callback = CALLBACK_WITH_ERRCHECK(func_with_errcheck)
callback(1, 2)

# Test ctypes.PYFUN
