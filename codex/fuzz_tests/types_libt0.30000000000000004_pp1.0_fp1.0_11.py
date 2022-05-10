import types
types.MethodType(lambda self: None, None)

# This should fail with an AttributeError.
try:
    types.MethodType(lambda self: None, None, None)
except AttributeError:
    print('AttributeError')

# This should fail with a TypeError.
try:
    types.MethodType(lambda self: None, None, None, None)
except TypeError:
    print('TypeError')
