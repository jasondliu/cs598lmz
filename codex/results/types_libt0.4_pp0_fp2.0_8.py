import types
types.MethodType(lambda self: self, None)

# Test that we can use a method as a class decorator.
def decorator(self):
    return self

@decorator
class C:
    pass

# Test that we can use a method as a function decorator.
@decorator
def f():
    pass

# Test that we can use a method as a method decorator.
class D:
    @decorator
    def f(self):
        pass

# Test that we can use a method as a staticmethod.
class E:
    f = staticmethod(decorator)

# Test that we can use a method as a classmethod.
class F:
    f = classmethod(decorator)

# Test that we can use a method as a property.
class G:
    f = property(decorator)

# Test that we can use a method as a super.
class H(object):
    def f(self):
        pass

class I(H):
    def f(self):
        super(I, self).f
