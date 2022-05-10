import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type, it takes an int and returns an int
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we want to call
func = lib.my_function

# Assign the function pointer type as restype to func
func.restype = f

# Call func() and get a function pointer
my_function = func()

# Call the function pointer
res = my_function(42)
print(res)

# This should fail, because the function pointer is not callable
# anymore
try:
    my_function(42)
except ValueError:
    print('ValueError')

# This should fail, because the function pointer is not callable
# anymore
try:
    func(42)
except ValueError:
    print('ValueError')

# This should fail, because the function pointer is not callable
# anymore
try:
    func()
