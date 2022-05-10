import weakref
# Test weakref.ref()
class C:
    pass
o = C()
r = weakref.ref(o)
assert r() is o
assert r() is not None
r = weakref.ref(o)
assert r() is o
del o
r()
r()
r()
r()
r()
r()
r()
r()
r()
r()
r()
r()
r()
r()
r()

# Test weakref.proxy()
class C:
    pass
o = C()
p = weakref.proxy(o)
assert p is o
assert p is not None
p = weakref.proxy(o)
assert p is o
del o
p
p
p
p
p
p
p
p
p
p
p
p
p
p

# Test weakref.getweakrefcount()
class C:
    pass
o = C()
assert weakref.getweakrefcount(o) == 0
p = weakref.proxy(o)
assert weakref.getweakrefcount(o) == 1
r = weakref
