import types
types.MethodType(lambda self: None, None, type)

# This should fail with a TypeError, but instead it fails with a
# SystemError.
try:
    types.MethodType(lambda self: None, None, type, 42)
except TypeError:
    pass
else:
    print('Expected TypeError')
