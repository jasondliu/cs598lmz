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
r1 = weakref.ref(a)
r2 = weakref.ref(a)
assert weakref.getweakrefcount(a) == 2

# Test weakref.getweakrefs()

class A:
    pass

a = A()
r1 = weakref.ref(a)
r2 = weakref.ref(a)
assert weakref.getweakrefs(a) == [r1, r2]

# Test weakref.finalize()


