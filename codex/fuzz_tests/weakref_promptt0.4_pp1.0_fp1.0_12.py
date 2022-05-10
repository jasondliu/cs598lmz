import weakref
# Test weakref.ref
class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
del o
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
    raise Exception, "expected ReferenceError"
# Test weakref.getweakrefcount
assert weakref.getweakrefcount(C()) == 0
# Test weakref.getweakrefs
assert weakref.getweakrefs(C()) == []
# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
o = C()
d[o] = 42
assert d[o] == 42
del o
assert len(d) == 0
# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
o = C()
d[42] = o
assert d[42] is o
del o
assert len(d) == 0
