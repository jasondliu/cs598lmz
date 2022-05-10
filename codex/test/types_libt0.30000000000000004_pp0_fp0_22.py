import types
types.MethodType(foo, None)

# This should fail
types.MethodType(foo, None, None)

# This should fail
types.MethodType(foo, None, None, None)

# This should fail
types.MethodType(foo, None, None, None, None)

# This should fail
types.MethodType(foo, None, None, None, None, None)

