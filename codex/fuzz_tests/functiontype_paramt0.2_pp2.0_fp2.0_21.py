from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# Test that we can't create a function with a non-string name
try:
    FunctionType(lambda: None, globals(), None)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a function with a non-dict globals
try:
    FunctionType(lambda: None, None, 'lambda')
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a function with a non-dict defaults
try:
    FunctionType(lambda: None, globals(), 'lambda', None)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a function with a non-string doc
try:
    FunctionType(lambda: None, globals(), 'lambda', (), None)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a function with a non-string dict
try:
