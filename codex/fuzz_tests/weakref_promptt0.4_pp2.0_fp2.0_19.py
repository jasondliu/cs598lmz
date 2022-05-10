import weakref
# Test weakref.ref(x) == weakref.ref(x)

class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'A(%r)' % self.x

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(D):
    pass

for base in A, B, C, D, E:
    x = base(42)
    y = base(42)
    rx = weakref.ref(x)
    ry = weakref.ref(y)
    assert rx == ry
    assert rx is not ry
    assert rx() is x
    assert ry() is y
    assert rx() is y
    assert ry() is x
    assert rx == y
    assert ry == x
    assert rx is not y
    assert ry is not x
    assert rx != id(x)
    assert ry != id(y)
   
