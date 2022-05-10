import ctypes
# Test ctypes.CFUNCTYPE

# This should print '1'
print(ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: x + 1)(0))

# This should print '2'
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def pyfunc(x):
    return x + 1

@ctypes.CFUNCTYPE(ctypes.c_int)
def pyfunc2(x):
    return x + 1

print(pyfunc(1))
print(pyfunc2(1))

# This should print '3'
@ctypes.CFUNCTYPE(ctypes.c_int)
def pyfunc3(x):
    return x + 1
@ctypes.CFUNCTYPE(ctypes.c_int)
def pyfunc4(x):
    return x + 1

print(pyfunc3(2))
print(pyfunc4(2))
# Test ctypes.byref

import ctypes

