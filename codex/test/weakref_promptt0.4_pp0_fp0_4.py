import weakref
# Test weakref.ref(class)
class C(object):
    pass
r = weakref.ref(C)
assert r().__name__ == 'C'

# Test weakref.ref(instance)
c = C()
r = weakref.ref(c)
assert r() is c

# Test weakref.ref(instancemethod)
class D(object):
    def f(self):
        pass
d = D()
r = weakref.ref(d.f)
assert r() is d.f

# Test weakref.ref(builtinmethod)
r = weakref.ref(D.f)
assert r() is D.f

# Test weakref.ref(classmethod)
class E(object):
    @classmethod
    def f(cls):
        pass
r = weakref.ref(E.f)
assert r() is E.f

# Test weakref.ref(staticmethod)
class F(object):
    @staticmethod
    def f():
        pass
r = weakref.ref(F.f)
