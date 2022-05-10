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

another_function = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int,
                                      ctypes.c_int)(another_function)
result = another_function(2, 3)
print(result)

# Test ctypes.PYFUNCTYPE
def yet_another_function(x, y):
    return x + y

yet_another_function = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int,
                                         ctypes.c_int)(yet_another_function)
result = yet_another_function(2, 3)
print(result)

# Test ctypes.PYFUN
