import weakref
# Test weakref.ref
class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
del o
assert r() is None
# Test weakref.proxy
class C:
    pass

o = C()
p = weakref.proxy(o)
assert p is o
del o
try:
    p
except ReferenceError:
    pass
