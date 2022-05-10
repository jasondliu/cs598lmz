import types
types.MethodType(foo, None, None)

# TypeError: unbound method foo() must be called with None instance as first argument (got nothing instead)
