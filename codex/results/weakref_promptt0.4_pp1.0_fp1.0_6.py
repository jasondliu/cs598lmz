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
else:
    raise Exception, "expected ReferenceError"

# Test weakref.getweakrefcount()

assert weakref.getweakrefcount(o) == 0
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1
p = weakref.proxy(o)
assert weakref.getweakrefcount(o) == 2
del r, p
assert weakref.getweakrefcount(o) == 0

# Test weakref.getweakrefs()

assert weakref.getweakrefs(o) == []
r = weakref.ref(o)
assert weakref.getweakrefs(o) == [r]
p = weakref.proxy(o)
assert weakref.getweakref
