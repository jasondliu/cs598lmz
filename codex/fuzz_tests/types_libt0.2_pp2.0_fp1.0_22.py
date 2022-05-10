import types
types.MethodType(lambda self: None, None, object)

# Test that we can't create a method with a non-function
# as the first argument.
try:
    types.MethodType(1, None, object)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a method with a non-class
# as the third argument.
try:
    types.MethodType(lambda self: None, None, 1)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a method with a non-instance
# as the second argument.
try:
    types.MethodType(lambda self: None, 1, object)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a method with a non-instance
# as the second argument.
try:
    types.MethodType(lambda self: None, 1, object)
except TypeError:
    pass
else:
    print("Expected Type
