import weakref
# Test weakref.ref(x)
class A:
    pass
a = A()
r = weakref.ref(a)
assert r() is a
assert r() is not None
del a
assert r() is None
# Test weakref.proxy(x)
class A:
    pass
a = A()
p = weakref.proxy(a)
assert p is a
assert p is not None
del a
try:
    p
except ReferenceError:
    pass
