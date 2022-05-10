from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo") for f in (lambda x: x, lambda y: y))

# Test that the __code__ attribute of a built-in function is writable.
def f(): pass
f.__code__ = type(f.__code__)(0, 0, 0, 0, b"", (), (), (), "", "", 0, b"")

# Test that the __code__ attribute of a built-in method is writable.
def f(): pass
f.__code__ = type(f.__code__)(0, 0, 0, 0, b"", (), (), (), "", "", 0, b"")

# Test that the __code__ attribute of a built-in method is writable.
def f(): pass
f.__code__ = type(f.__code__)(0, 0, 0, 0, b"", (), (), (), "", "", 0, b"")

# Test that the __code__ attribute of a built-in method is writable.
def f(): pass
f.__code__ = type(f.__code__)(
