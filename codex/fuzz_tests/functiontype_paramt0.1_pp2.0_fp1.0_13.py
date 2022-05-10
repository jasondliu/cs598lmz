from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that the repr of a function is not affected by the presence of a
# __qualname__ attribute.
def f(): pass
f.__qualname__ = 'foo'
repr(f)

# Test that the repr of a function is not affected by the presence of a
# __module__ attribute.
def f(): pass
f.__module__ = 'foo'
repr(f)

# Test that the repr of a function is not affected by the presence of a
# __defaults__ attribute.
def f(): pass
f.__defaults__ = (1, 2, 3)
repr(f)

# Test that the repr of a function is not affected by the presence of a
# __kwdefaults__ attribute.
def f(): pass
f.__kwdefaults__ = {'a': 1, 'b': 2, 'c': 3}
repr(f)

# Test that the repr of a function is not affected by the presence of a
# __annotations__ attribute.
def f(): pass
f.__
