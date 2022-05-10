from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that the repr of a function with a __qualname__ works
def f():
    pass
f.__qualname__ = 'foo'
repr(f)

# Test that the repr of a function with a __qualname__ works
def f():
    pass
f.__qualname__ = 'foo.bar'
repr(f)

# Test that the repr of a function with a __qualname__ works
def f():
    pass
f.__qualname__ = 'foo.bar.baz'
repr(f)

# Test that the repr of a function with a __qualname__ works
def f():
    pass
f.__qualname__ = 'foo.bar.baz.qux'
repr(f)

# Test that the repr of a function with a __qualname__ works
def f():
    pass
f.__qualname__ = 'foo.bar.baz.qux.quux'
repr(f)

# Test that the repr of a function with a __
