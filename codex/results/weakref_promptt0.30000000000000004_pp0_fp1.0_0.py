import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

class D(C):
    pass

o = D()
r = weakref.ref(o)
assert r() is o

class E:
    def __init__(self, x):
        self.x = x

o = E(42)
r = weakref.ref(o)
assert r().x == 42

class F(E):
    def __init__(self, x):
        E.__init__(self, x)

o = F(42)
r = weakref.ref(o)
assert r().x == 42

# Test weakref.ref(obj, callback)

class C:
    pass

o = C()
r = weakref.ref(o, lambda x: None)
assert r() is o

class D(C):
    pass

o = D()
r = weakref.ref(o, lambda x: None)
assert r() is o


