import ctypes
# Test ctypes.CFUNCTYPE

@CFUNCTYPE(c_int, c_int)
def func(x):
    return x * x

assert func(5) == 25
assert func(c_int(5)) == 25
assert func(5) == func(c_int(5))

# Test ctypes.POINTER

@CFUNCTYPE(c_int, POINTER(c_int))
def func(x):
    return x[0] * x[0]

assert func(pointer(c_int(5))) == 25

# Test ctypes.py_object

@CFUNCTYPE(c_int, py_object)
def func(x):
    return x * x

assert func(5) == 25
assert func(c_int(5)) == 25
assert func(5) == func(c_int(5))

@CFUNCTYPE(c_int, py_object, POINTER(c_int))
def func(x, y):
    return x * y[0]

assert func(5, pointer(c_int
