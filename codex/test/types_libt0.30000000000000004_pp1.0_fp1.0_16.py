import types
types.MethodType(lambda self: None, None, cls)

# Test that we can't create a method on a class that is not a type
try:
    types.MethodType(lambda self: None, None, object())
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a method on a class that is not a type
try:
    types.MethodType(lambda self: None, None, object)
except TypeError:
    pass
else:
    print("Expected TypeError")

# Test that we can't create a method on a class that is not a type
try:
    types.MethodType(lambda self: None, None, type)
except TypeError:
    pass
