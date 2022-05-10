import types
types.MethodType(lambda self: None, None)

# Test that we can't create a MethodType with a non-function
try:
    types.MethodType(1, None)
except TypeError:
    pass
else:
    print("Should have raised TypeError")

# Test that we can't create a MethodType with a non-class
try:
    types.MethodType(lambda self: None, 1)
except TypeError:
    pass
else:
    print("Should have raised TypeError")

# Test that we can't create a MethodType with a non-class
try:
    types.MethodType(lambda self: None, "")
except TypeError:
    pass
else:
    print("Should have raised TypeError")

# Test that we can't create a MethodType with a non-class
try:
    types.MethodType(lambda self: None, 1.0)
except TypeError:
    pass
else:
    print("Should have raised TypeError")

# Test that we can't create a MethodType with a non-class
try:
    types.MethodType
