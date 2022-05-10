import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return object()
assert fun() == object()

# Trick the CPython compiler into thinking that the function
# uses the object in its body.
def g(x):
    assert x == object()
    return x
g(object())

# This should now annotate the function as returning and
# receiving a non-constant value.
assert not const(fun()) and not const(fun())

# Check that the function is not actually constant.
assert not constant_function(fun)

# Check that the function is not constant, but its value is.
assert not constant_function(fun()) and constant(fun())

# Check that the function is not constant, but its value is.
assert not constant_function(fun) and constant(fun)

@const
@constant_function
def h():
    return fun()

# Check that the function is constant, and also its value.
assert constant_function(h) and constant(h)
assert constant_function(h()) and constant(h())

# Check that the function is constant, but not its value.
assert constant_function(fun)
