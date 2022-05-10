from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo"))

# Test that we can't create a function with a non-string name
try:
    FunctionType(f.__code__, globals(), 0)
except TypeError:
    pass
else:
    print("Should have raised TypeError")

# Test that we can't create a function with a non-dict globals
try:
    FunctionType(f.__code__, 0, "foo")
except TypeError:
    pass
else:
    print("Should have raised TypeError")
