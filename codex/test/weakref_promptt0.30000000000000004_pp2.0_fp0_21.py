import weakref
# Test weakref.ref()

class C(object):
    pass

o = C()
r = weakref.ref(o)

assert r() is o
assert r() is not None

del o

assert r() is None

# Test weakref.proxy()

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

assert weakref.getweakrefcount(C()) == 0

o = C()
r = weakref.ref(o)

assert weakref.getweakrefcount(o) == 1

del o

assert weakref.getweakrefcount(r) == 0

# Test weakref.getweakrefs()

assert weakref.getweakrefs(C()) == []

o = C()
r = weakref.ref(o)

assert weakref.getweakrefs(o) == [r]


