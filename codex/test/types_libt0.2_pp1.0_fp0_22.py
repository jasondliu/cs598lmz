import types
types.MethodType(lambda self: self.x, None)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got int instance instead)
types.MethodType(lambda self: self.x, 1)

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got str instance instead)
types.MethodType(lambda self: self.x, 'str')

# TypeError: unbound method <lambda>() must be called with None instance as first argument (got list instance instead)
types.MethodType(lambda self: self.x, [])
