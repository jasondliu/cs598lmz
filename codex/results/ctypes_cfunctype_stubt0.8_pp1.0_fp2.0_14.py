import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

@fun.dispatch(object)
def fun_object(x):
    return "fun-object"

assert fun("x") == "fun-object"
assert fun(2) == "fun-object"
assert fun(object()) == "fun-object"
assert fun(3.0) == "fun-object"

# The disambiguation algorithm produces an error message if there
# are multiple default implementations:

def fun(x):
    return "fun"

@fun.dispatch(object)
def fun_object(x):
    return "fun-object"

@fun.dispatch(type(None))
def fun_object(x):
    return "fun-None"

try:
    fun(None)
except TypeError as e:
    assert str(e) == "multiple default implementations for 'fun' found"
else:
    raise Exception("DID NOT RAISE")

# Make sure we can delete a fall-back implementation of a class method:

class A(object):
    @classmethod
    @dispatch
