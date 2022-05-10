import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

del o
assert r() is None

# Test weakref.proxy()

p = weakref.proxy(o)
try:
    p.foo
except ReferenceError:
    pass
