import ctypes
# Test ctypes.CFUNCTYPE
# ctypes.CFUNCTYPE(<restype>, <argtypes>)
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def Add(a, b):
    return a + b

Add(1, 2)
# 3

Add.__name__
# 'Add'

Add.__doc__
# None

Add.__module__
# '__main__'

# Test ctypes.PYFUNCTYPE
# ctypes.PYFUNCTYPE(<restype>, <argtypes>)
@ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def Add(a, b):
    return a + b

Add(1, 2)
# 3

Add.__name__
# 'Add'

Add.__doc__
# 'Add(a, b) -> int'

Add.__module__
# '__main__'
