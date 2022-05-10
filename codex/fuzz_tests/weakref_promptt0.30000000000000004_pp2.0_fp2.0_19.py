import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
assert r() is a

a = None
assert r() is None
# Test weakref.proxy()

class A:
    pass

a = A()
p = weakref.proxy(a)
assert p is a

a = None
try:
    p.foo
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")
# Test weakref.getweakrefcount()

class A:
    pass

a = A()
r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1

a = None
assert weakref.getweakrefcount(r) == 1
# Test weakref.getweakrefs()

class A:
    pass

a = A()
r = weakref.ref(a)
assert weakref.getweakrefs(a) == [r]

a = None
assert weakref.getweakrefs(r) == []
# Test weakref
