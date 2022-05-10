from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo") for f in (lambda x: x, lambda y: y))

# Test that the __code__ attribute of a built-in function is writable.
def f(): pass
