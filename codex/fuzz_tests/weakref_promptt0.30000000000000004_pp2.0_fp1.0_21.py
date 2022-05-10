import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
assert r() is a

# Test weakref.proxy()

a = A()
p = weakref.proxy(a)
assert p is a

# Test weakref.getweakrefcount()

a = A()
assert weakref.getweakrefcount(a) == 0

r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1

p = weakref.proxy(a)
assert weakref.getweakrefcount(a) == 2

# Test weakref.getweakrefs()

a = A()
assert weakref.getweakrefs(a) == []

r = weakref.ref(a)
assert weakref.getweakrefs(a) == [r]

p = weakref.proxy(a)
assert weakref.getweakrefs(a) == [r, p]

# Test weakref.finalize()

class A:
    pass

a = A()
