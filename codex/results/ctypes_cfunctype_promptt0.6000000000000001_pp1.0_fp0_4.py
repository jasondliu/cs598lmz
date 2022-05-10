import ctypes
# Test ctypes.CFUNCTYPE(None)

def func():
    pass

c_func = ctypes.CFUNCTYPE(None)(func)

print(c_func.__name__)
print(c_func.__module__)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

c_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

print(c_func.__name__)
print(c_func.__module__)

# Test ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_char), ctypes.c_int)

def func(a):
    return str(a)

c_func = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_char), ctypes.c_int)(func)

print(c_func.__name__)
print(
