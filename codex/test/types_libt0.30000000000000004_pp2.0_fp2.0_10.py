import types
types.MethodType(lambda self: None, None, A)

# Test that we can't create a method with a non-callable
try:
    types.MethodType(1, None, A)
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that we can't create a method with a non-class
try:
    types.MethodType(lambda self: None, None, 1)
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that we can't create a method with a non-instance
try:
    types.MethodType(lambda self: None, 1, A)
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that we can't create a method with a non-instance
try:
    types.MethodType(lambda self: None, 1, A)
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that we can't create a method with a non-instance
