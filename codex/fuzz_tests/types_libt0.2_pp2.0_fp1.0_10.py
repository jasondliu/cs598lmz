import types
types.MethodType(lambda self: self, None)

# Test that we can create a MethodType with a function that takes
# *args and **kwargs.
def f(self, *args, **kwargs):
    return self
types.MethodType(f, None)

# Test that we can create a MethodType with a function that takes
# *args and **kwargs, and call it with *args and **kwargs.
def f(self, *args, **kwargs):
    return self, args, kwargs
types.MethodType(f, None)(1, 2, 3, a=4, b=5, c=6)

# Test that we can create a MethodType with a function that takes
# *args and **kwargs, and call it with no arguments.
def f(self, *args, **kwargs):
    return self, args, kwargs
types.MethodType(f, None)()

# Test that we can create a MethodType with a function that takes
# *args and **kwargs, and call it with only *args.
def f(self, *
