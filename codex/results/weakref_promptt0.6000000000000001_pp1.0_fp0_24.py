import weakref
# Test weakref.ref
class A:
    pass
a = A()
r = weakref.ref(a)
assert r() is a
del a
assert r() is None

# Test weakref.proxy
class A:
    pass
a = A()
p = weakref.proxy(a)
assert p is a
del a
try:
    p
except ReferenceError:
    pass

# Test weakref.getweakrefcount
class A:
    pass
a = A()
assert weakref.getweakrefcount(a) == 0
r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1
del r
assert weakref.getweakrefcount(a) == 0

# Test weakref.getweakrefs
class A:
    pass
a = A()
r1 = weakref.ref(a)
assert weakref.getweakrefs(a) == [r1]
r2 = weakref.ref(a)
assert weakref.getweakrefs(a) == [r1, r2]
del r1
assert
