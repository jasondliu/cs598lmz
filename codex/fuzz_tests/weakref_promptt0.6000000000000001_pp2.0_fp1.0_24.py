import weakref
# Test weakref.ref
class A: pass
a = A()
r = weakref.ref(a)
assert r() is a
del a
assert r() is None

# Test bound methods
class A:
    def f(self):
        return 42

a = A()
r = weakref.ref(a.f)
assert r()(a) == 42

# Test static methods
class A:
    @staticmethod
    def f():
        return 42

a = A()
r = weakref.ref(a.f)
assert r()() == 42

# Test class methods
class A:
    @classmethod
    def f(cls):
        return 42

a = A()
r = weakref.ref(a.f)
assert r()() == 42

# Test weakref.proxy
class A: pass
a = A()
p = weakref.proxy(a)
assert p is a
del a
try:
    p.x
    assert 0
except ReferenceError:
    pass

# Test weakref.finalize
class A: pass

