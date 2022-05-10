import types
types.MethodType(lambda self, x: x, None, Foo)

# Test that we can get/set attributes on a class.
Foo.bar = 'bar'
assert Foo.bar == 'bar'

# Test that we can delete attributes on a class.
del Foo.bar

try:
    print(Foo.bar)
    assert False
except AttributeError:
    pass

# Test that we can define a class method.
class Foo:
    def bar(self):
        pass
    bar = classmethod(bar)

# Test that we can define a static method.
class Foo:
    def bar(self):
        pass
    bar = staticmethod(bar)

# Test that we can define a property.
class Foo:
    def getx(self): return self._x
    def setx(self, value): self._x = value
    def delx(self): del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

# Test that we can define a class with slots.
