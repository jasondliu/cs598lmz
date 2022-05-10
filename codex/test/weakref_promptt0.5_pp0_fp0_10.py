import weakref
# Test weakref.ref()

def f(x):
    return x

class C(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

class D(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x
    def __hash__(self):
        return hash(self.x)

for x in [None,
          42,
          2**100,
          -2**100,
          2**10000,
          -2**10000,
          1.25,
          1+2j,
          'abc',
          tuple(range(10)),
          f,
          C(42),
          D(42),
          ]:
    a = weakref.ref(x)
    b = weakref.ref(x)
    assert a() is x
    assert b() is x
    assert a is not b
    assert a == b
    assert hash(a) == hash(b)
