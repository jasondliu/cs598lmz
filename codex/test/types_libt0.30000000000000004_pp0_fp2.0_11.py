import types
types.MethodType(lambda self, x: x, None, Foo)

# Test that we can create a new method from an existing method
# and a new class
def f(self, x):
    return x

Foo.f = types.MethodType(f, None, Foo)

# Test that we can create a new method from an existing method
# and a new class, using the same name as the existing method
def g(self, x):
    return x

Foo.f = types.MethodType(g, None, Foo)

# Test that we can create a new method from an existing method
# and a new class, using the same name as the existing method
# and the same class as the existing method
def h(self, x):
    return x

Foo.f = types.MethodType(h, None, Foo)

# Test that we can create a new method from an existing method
# and a new class, using the same name as the existing method
# and the same class as the existing method, but with a different
# function
def i(self, x):
    return x
