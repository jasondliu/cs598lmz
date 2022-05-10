import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

assert r() is o
assert r() is not None

del o

assert r() is None
# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)

assert p is o

del o

try:
    p.foo
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")
# Test weakref.getweakrefcount()

class C:
    pass

o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)

assert weakref.getweakrefcount(o) == 2

del r1

assert weakref.getweakrefcount(o) == 1

del r2

assert weakref.getweakrefcount(o) == 0
# Test weakref.getweakrefs()

class C:
    pass

o = C()
r1 = weakref.
