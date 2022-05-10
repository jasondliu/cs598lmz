import types
types.MethodType(lambda self: 42, None)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
types.MethodType(lambda self: 42, 42)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
types.MethodType(lambda self: 42, 'str')

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
types.MethodType(lambda self: 42, 1.0)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
types.MethodType(lambda self: 42, 3+4j)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
types.MethodType(lambda self: 42, [])

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
types.MethodType(
