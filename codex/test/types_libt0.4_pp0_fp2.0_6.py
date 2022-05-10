import types
types.MethodType(lambda self: 42, None)

# Test the basic functionality of the method type.
class C:
    def f(self, x):
        return x

c = C()
m = types.MethodType(c.f, c)
