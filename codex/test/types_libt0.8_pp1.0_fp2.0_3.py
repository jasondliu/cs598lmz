import types
types.MethodType(foo, instance)

# this is the correct way
instance.foo = types.MethodType(foo, instance)

# then we can call it
