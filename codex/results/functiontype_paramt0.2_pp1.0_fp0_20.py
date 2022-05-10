from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), 'foo'))

# Test that a function with a __code__ that is not a code object
# raises a TypeError.
def f():
    pass
f.__code__ = 'not a code object'
try:
    list(FunctionType(f.__code__, globals(), 'foo'))
except TypeError:
    pass
else:
    print('TypeError not raised')

# Test that a function with a __code__ that is a code object
# with a non-string co_name raises a TypeError.
def f():
    pass
f.__code__.co_name = 42
try:
    list(FunctionType(f.__code__, globals(), 'foo'))
except TypeError:
    pass
else:
    print('TypeError not raised')

# Test that a function with a __code__ that is a code object
# with a non-string co_filename raises a TypeError.
def f():
    pass
f.__code__.co_filename = 42
try:
    list(Function
