from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that we can't create a function with a non-string name
try:
    FunctionType(lambda: None, globals(), None)
except TypeError:
    pass
else:
    print("Didn't raise TypeError")

# Test that we can't create a function with a non-string docstring
try:
    FunctionType(lambda: None, globals(), 'foo', None)
except TypeError:
    pass
else:
    print("Didn't raise TypeError")

# Test that we can't create a function with a non-tuple closure
try:
    FunctionType(lambda: None, globals(), 'foo', '', None)
except TypeError:
    pass
else:
    print("Didn't raise TypeError")

# Test that we can't create a function with a non-string annotation
try:
    FunctionType(lambda: None, globals(), 'foo', '', (), None)
except TypeError:
    pass
else:
    print("Didn't raise TypeError")

# Test
