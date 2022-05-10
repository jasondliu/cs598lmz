from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that the __code__ attribute of a function is read-only
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("shouldn't be able to assign to __code__")

# Test that the __code__ attribute of a function is writable
def f(): pass
try:
    f.__code__ = f.__code__
except TypeError:
    print("should be able to assign to __code__")

# Test that the __code__ attribute of a function is writable
def f(): pass
try:
    f.__code__ = f.__code__
except TypeError:
    print("should be able to assign to __code__")

# Test that the __code__ attribute of a function is writable
def f(): pass
try:
    f.__code__ = f.__code__
except TypeError:
    print("should be able to assign to __code__")

# Test that the __code__ attribute of a function is writ
