import types
types.MethodType(lambda self: None, None, None)

# This should be rejected because the first argument is not a type
types.MethodType(lambda self: None, None)

# This should be rejected because the first argument is not a type
types.MethodType(lambda self: None)

