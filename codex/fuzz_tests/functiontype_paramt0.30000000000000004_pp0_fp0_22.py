from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), "foo")(1))

# Test that the repr of a function with a __qualname__ is correct
def f(): pass
f.__qualname__ = "foo"
repr(f)

# Test that the repr of a function with a __qualname__ and a __module__ is correct
def f(): pass
f.__qualname__ = "foo"
f.__module__ = "bar"
repr(f)

# Test that the repr of a function with a __qualname__ and a __module__ is correct
def f(): pass
f.__qualname__ = "foo"
f.__module__ = "bar"
f.__doc__ = "doc"
repr(f)

# Test that the repr of a function with a __qualname__ and a __module__ is correct
def f(): pass
f.__qualname__ = "foo"
f.__module__ = "bar"
f.__doc__ = "doc"
f.__defaults__ = (1, 2)
repr(f)

