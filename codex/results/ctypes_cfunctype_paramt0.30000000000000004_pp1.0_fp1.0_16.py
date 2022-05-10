import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

f = FUNTYPE(func)
print f(1, 2)

f = FUNTYPE(lambda a, b: a + b)
print f(1, 2)

f = FUNTYPE(lambda a, b: a + b, use_errno=True)
print f(1, 2)

f = FUNTYPE(lambda a, b: a + b, use_last_error=True)
print f(1, 2)

f = FUNTYPE(lambda a, b: a + b, use_errno=True, use_last_error=True)
print f(1, 2)

f = FUNTYPE(lambda a, b: a + b, use_errno=True, use_last_error=True,
            save_errno=True)
print f(1, 2)

f = FUNTYPE(lambda a, b: a + b, use_errno=True, use_last_error
