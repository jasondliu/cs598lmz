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
else:
    raise Exception, "expected ReferenceError"
# Test weakref.getweakrefcount(x)
class A:
    pass
a = A()
assert weakref.getweakrefcount(a) == 0
r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1
del r
assert weakref.getweakrefcount(a) == 0
# Test weakref.getweakrefs(x)
class A:
    pass
a = A()
assert weakref.getweakrefs(a) == []
r = weakref.ref(a)
assert weakref.get
