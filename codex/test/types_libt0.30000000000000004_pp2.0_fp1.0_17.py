import types
types.MethodType(lambda self: None, None, object)

# Test that we can define a method with a non-string name
# and a non-string docstring.
def f(self):
    pass
f.__name__ = 1
f.__doc__ = 1
class C:
    method = f

# Test that we can define a method with a non-string name
# and a non-string docstring.
def f(self):
    pass
f.__name__ = 1
f.__doc__ = 1
class C:
    method = types.MethodType(f, None)

# Test that we can define a method with a non-string name
# and a non-string docstring.
def f(self):
    pass
f.__name__ = 1
f.__doc__ = 1
class C:
    method = types.MethodType(f, None, object)

# Test that we can define a method with a non-string name
# and a non-string docstring.
def f(self):
    pass
f.__name__ = 1
f
