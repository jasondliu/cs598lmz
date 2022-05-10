import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
assert r() is o
del o
assert r() is None
assert r() is None
# Test weakref.proxy
class C:
    pass
o = C()
p = weakref.proxy(o)
assert p is o
del o
try:
    p
except ReferenceError:
    pass
else:
    raise Exception
# Test weakref.getweakrefcount
class C:
    pass
o = C()
assert weakref.getweakrefcount(o) == 0
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1
del r
assert weakref.getweakrefcount(o) == 0
# Test weakref.getweakrefs
class C:
    pass
o = C()
assert weakref.getweakrefs(o) == []
r = weakref.ref(o)
assert weakref.getweakrefs(o) == [r]
del r
assert weakref.getweakrefs(o)
