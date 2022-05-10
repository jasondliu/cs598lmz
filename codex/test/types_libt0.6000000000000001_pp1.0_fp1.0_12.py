import types
types.MethodType(f, x)

# types.MethodType(f, x)
# TypeError: unbound method f() must be called with X instance as first argument (got nothing instead)

x.f()

x.f = types.MethodType(f, x)

x.f()
# f()
# <__main__.X instance at 0x7f9d9c2c1e18>
# f()
# <__main__.X instance at 0x7f9d9c2c1e18>

# types.MethodType(f, None, X)
# TypeError: unbound method f() must be called with X instance as first argument (got nothing instead)

# types.MethodType(f, x, X)
# TypeError: unbound method f() must be called with X instance as first argument (got nothing instead)

# types.MethodType(f, x, X)
# TypeError: unbound method f() must be called with X instance as first argument (got nothing instead)

types.MethodType(f, None, X)


