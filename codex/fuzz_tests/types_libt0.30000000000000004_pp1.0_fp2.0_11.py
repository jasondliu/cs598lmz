import types
types.MethodType(lambda self, x: x, None, None)

# This should fail
try:
    types.MethodType(lambda self, x: x, None)
except TypeError:
    print('TypeError')

# This should fail
try:
    types.MethodType(lambda self, x: x, None, None, None)
except TypeError:
    print('TypeError')
