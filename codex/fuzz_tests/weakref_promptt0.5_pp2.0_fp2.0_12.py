import weakref
# Test weakref.ref

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

del o
gc.collect()
assert r() is None

# Test weakref.proxy

o = C()
p = weakref.proxy(o)
assert p is o

del o
gc.collect()
try:
    p.foo
except ReferenceError:
    pass
else:
    assert False, "should have raised ReferenceError"

# Test weakref.getweakrefcount

o = C()
assert weakref.getweakrefcount(o) == 0
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1
p = weakref.proxy(o)
assert weakref.getweakrefcount(o) == 2

# Test weakref.getweakrefs

assert len(weakref.getweakrefs(o)) == 2

# Test weakref.finalize

# Test weakref.finalize with an object

class Foo:
    pass

def callback(
