import types
types.MethodType(lambda self: None, None, Dummy)

# does not work with other types, or unsubscriptable objects
try:
    types.MethodType(lambda self: None, None, 42)
except TypeError:
    print('TypeError')

try:
    types.MethodType(lambda self: None, None, Dummy())
except TypeError:
    print('TypeError')
