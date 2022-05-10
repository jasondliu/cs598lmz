from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that the __code__ attribute of a function is read-only
def f():
    pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("f.__code__ = None should have raised TypeError")

# Test that the __code__ attribute of a function is writable
# when the function is created with types.FunctionType
def f():
    pass
try:
    types.FunctionType(f.__code__, globals(), 'foo')
except TypeError:
    print("types.FunctionType(f.__code__, globals(), 'foo') should not have raised TypeError")

# Test that the __code__ attribute of a function is writable
# when the function is created with types.FunctionType
def f():
    pass
try:
    types.FunctionType(f.__code__, globals(), 'foo')
except TypeError:
    print("types.FunctionType(f.__code__, globals(), 'foo') should not have raised TypeError")
