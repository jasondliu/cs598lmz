import types
types.MethodType(foo, None)

# TypeError: unbound method foo() must be called with None instance as first argument (got int instance instead)
types.MethodType(foo, 1)

# TypeError: unbound method foo() must be called with None instance as first argument (got str instance instead)
types.MethodType(foo, 'bar')

# TypeError: unbound method foo() must be called with None instance as first argument (got list instance instead)
types.MethodType(foo, [])

# TypeError: unbound method foo() must be called with None instance as first argument (got dict instance instead)
types.MethodType(foo, {})

# TypeError: unbound method foo() must be called with None instance as first argument (got set instance instead)
types.MethodType(foo, set())

# TypeError: unbound method foo() must be called with None instance as first argument (got frozenset instance instead)
types.MethodType(foo, frozenset())

# TypeError: unbound method foo() must be called with None instance as first argument (got tuple instance instead)

