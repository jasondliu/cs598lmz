from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo'))

# Test that the repr of a function is not affected by the presence of a
# __qualname__ attribute.
def f(): pass
f.__qualname__ = 'foo'
repr(f)

# Test that the repr of a function is not affected by the presence of a
# __text_signature__ attribute.
def f(): pass
f.__text_signature__ = 'foo'
repr(f)

# Test that the repr of a function is not affected by the presence of a
# __closure__ attribute.
def f(): pass
f.__closure__ = 'foo'
repr(f)

# Test that the repr of a function is not affected by the presence of a
# __annotations__ attribute.
def f(): pass
f.__annotations__ = 'foo'
repr(f)

# Test that the repr of a function is not affected by the presence of a
# __kwdefaults__ attribute.
def f(): pass
f.__kwdefaults__ = 'foo'
repr(f
