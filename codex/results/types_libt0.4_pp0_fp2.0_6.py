import types
types.MethodType(lambda self: 42, None)

# Test the basic functionality of the method type.
class C:
    def f(self, x):
        return x

c = C()
m = types.MethodType(c.f, c)
print m(42)

# Test that the __func__ attribute is set correctly.
print m.__func__ is c.f

# Test that the __self__ attribute is set correctly.
print m.__self__ is c

# Test that the __name__ attribute is set correctly.
print m.__name__ == 'f'

# Test that the __doc__ attribute is set correctly.
print m.__doc__ == 'f(self, x)\n\n    '

# Test that the __module__ attribute is set correctly.
print m.__module__ == '__main__'

# Test that the __dict__ attribute is set correctly.
print m.__dict__ == {}

# Test that the __get__ method works correctly.
print m.__get__(None, C) is m
print m.__get
