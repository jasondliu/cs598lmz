import types
types.MethodType(lambda self: None, None, None)

# Test that we can create a MethodType with a function with a __slots__
# attribute.
class f(object):
    __slots__ = []
def g():
    pass
g.__slots__ = []
types.MethodType(f, None)
types.MethodType(g, None)

# Test that we can create a MethodType with a function with a __dict__
# attribute.
def h():
    pass
h.__dict__ = {}
types.MethodType(h, None)

# Test that we can create a MethodType with a function with a __doc__
# attribute.
def i():
    pass
i.__doc__ = ""
types.MethodType(i, None)

# Test that we can create a MethodType with a function with a __name__
# attribute.
def j():
    pass
j.__name__ = ""
types.MethodType(j, None)

# Test that we can create a MethodType with a function with a __module__
# attribute.
