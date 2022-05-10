import types
types.MethodType(lambda self: 42, list(), list)  # Matches
types.MethodType(lambda self: 42, list(), int)  # Doesn't match

