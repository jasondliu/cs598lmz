import types
types.MethodType(lambda self: None, None, object)

# Test that we can create a bound method with a non-callable object
# as the second argument.
try:
    types.MethodType(lambda self: None, None, None)
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that we can create a bound method with a non-callable object
# as the first argument.
try:
    types.MethodType(None, None, object)
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that we can create a bound method with a non-callable object
# as the first argument.
try:
    types.MethodType(None, None, None)
except TypeError:
    pass
else:
    print("expected TypeError")

# Test that we can create a bound method with a non-callable object
# as the first argument.
try:
    types.MethodType(None, None, None)
except TypeError:
    pass
else:
    print("expected TypeError")
