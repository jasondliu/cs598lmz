import types
types.MethodType(lambda self: None, None, cls)

# Test that we can't create a method with a non-function
try:
    types.MethodType(1, None, cls)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a method with a non-class
try:
    types.MethodType(lambda self: None, None, 1)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a method with a non-instance
try:
    types.MethodType(lambda self: None, 1, cls)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a method with a non-instance
try:
    types.MethodType(lambda self: None, 1, cls)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a method with a non-instance
try:
    types
