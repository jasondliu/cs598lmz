import ctypes
# Test ctypes.CFUNCTYPE
def a_function(x):
    return x + 1

a_function = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(a_function)
result = a_function(2)
print(result)

# Test ctypes.WINFUNCTYPE
def another_function(x, y):
    return x + y

