import weakref
# Test weakref.ref() when key is the object itself
# the behavior of weakref.ref in this case is intentionally undefined
with pytest.raises(TypeError):
    weakref.ref(42)
with pytest.raises(TypeError):
    weakref.ref('string')
def g(x):
    return x.value

def f(x):
    return weakref.ref(x, g)

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'A(%r)' % self.value
    def __eq__(self, other):
        return self.value == other.value

class B:
    def __del__(self):
        pass

a = A(42)
r = f(a)
with pytest.raises(ReferenceError):
    r()
b = B()
rb = f(b)
with pytest.raises(ReferenceError):
    rb() # exception from __del__() is silently ignored

a = A(25)
d
