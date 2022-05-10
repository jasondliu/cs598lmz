import ctypes
# Test ctypes.CFUNCTYPE

#################################################################

# define int func(int)
FUNC_INT_INT = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# call func(3) == 6
def func(x):
    return x+3

# test a C function: get its address and coerce it to a python object
ca = ctypes.cast(func, FUNC_INT_INT)
assert ca(2) == func(2) == 2+3
# test a python callable
fa = ctypes.cast(func, FUNC_INT_INT)
assert fa(2) == func(2) == 2+3

class error(IOError):
    pass
err = ctypes.cast(error, FUNC_INT_INT)
exc = raises(error, err, 42)
assert isinstance(exc, error)
assert exc.args == (42,)

#################################################################

# define void func(int **, int *, int[10])
FUNC_INT2_INT1_INT10 = ctypes.CFUNCT
