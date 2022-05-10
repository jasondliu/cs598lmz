import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
assert fun() == 1

# Test returning a function from a function
@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 1
assert fun() == 1

# Test returning a function from a function, with a nested function
@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    @ctypes.CFUNCTYPE(ctypes.py_object)
    def nested():
        return 1
    return nested
assert fun()() == 1

# Test returning a function from a function, with a nested function,
# and call the nested function
@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    @ctypes.CFUNCTYPE(ctypes.py_object)
    def nested():
        return 1
    return nested()
assert fun() == 1

# Test returning a function from a function, with a nested function,
# and call the nested function, with a closure
@ctypes.CFUNCTYPE(ctypes.py_object
