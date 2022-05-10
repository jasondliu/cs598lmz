from types import FunctionType
list(FunctionType(lambda: 1, globals(), "lambda"))

# Test that the repr of a function is accurate.
def f():
    pass
assert repr(f) == "<function f at %x>" % id(f)
assert repr(f.__code__) == "<code object f at %x, file '%s', line 1>" % (id(f.__code__), __file__)

# Test that the repr of a function with a docstring is accurate.
def f():
    """docstring"""
    pass
assert repr(f) == "<function f at %x>" % id(f)
assert repr(f.__code__) == "<code object f at %x, file '%s', line 1>" % (id(f.__code__), __file__)

# Test that the repr of a function with a closure is accurate.
def f(x):
    def g(y):
        return x + y
    return g
assert repr(f(1)) == "<function f.<locals>.g at %x>" % id(f(1))
assert repr(f(1).
