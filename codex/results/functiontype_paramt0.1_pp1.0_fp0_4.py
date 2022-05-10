from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that the __code__ attribute of a function is a code object.
def f(): pass
assert isinstance(f.__code__, types.CodeType)

# Test that the __code__ attribute of a function is writable.
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Test that the __code__ attribute of a function is writable.
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Test that the __code__ attribute of a function is writable.
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Test that the __code__ attribute of a function is writable.
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Test that the __code__ attribute of a function is writable.
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Test that the __code__ attribute
