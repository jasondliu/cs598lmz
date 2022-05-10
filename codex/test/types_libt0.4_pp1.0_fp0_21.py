import types
types.MethodType(lambda self: 42, None)

# TypeError: unbound method must be called with instance as first argument
# (got nothing instead)

# https://stackoverflow.com/questions/1015307/python-bind-an-unbound-method

# The following works:

def f(self):
    return 42

types.MethodType(f, None)()

# 42
