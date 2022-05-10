import types
types.MethodType(lambda self, x: x, None)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
# types.MethodType(lambda self, x: x, None)(1)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
# types.MethodType(lambda self, x: x, None)(1, 2)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
# types.MethodType(lambda self, x: x, None)(1, 2, 3)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
# types.MethodType(lambda self, x: x, None)(1, 2, 3, 4)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
