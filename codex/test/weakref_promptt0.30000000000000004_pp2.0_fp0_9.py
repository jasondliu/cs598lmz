import weakref
# Test weakref.ref()

class A(object):
    pass

a = A()
r = weakref.ref(a)
assert r() is a
del a
assert r() is None

# Test weakref.proxy()

class A(object):
    pass

a = A()
p = weakref.proxy(a)
assert p is a
del a
try:
    p.foo
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")

# Test weakref.getweakrefcount()

class A(object):
    pass

a = A()
assert weakref.getweakrefcount(a) == 0
r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1
p = weakref.proxy(a)
assert weakref.getweakrefcount(a) == 2
del r, p
assert weakref.getweakrefcount(a) == 0

# Test weakref.getweakrefs()

class A(object):
    pass

a = A()
