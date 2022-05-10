import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

# Callback function
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Convert function to callback
cmp_func = CMPFUNC(func)

# Call callback
print(cmp_func(1, 2))

# Test ctypes.WINFUNCTYPE
def func(a, b):
    return a + b

# Callback function
CMPFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Convert function to callback
cmp_func = CMPFUNC(func)

# Call callback
print(cmp_func(1, 2))

# Test ctypes.PYFUNCTYPE
def func(a, b):
    return a + b

# Callback function
CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_
