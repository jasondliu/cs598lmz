import weakref
# Test weakref.ref(obj)
class C: pass
obj = C()
r = weakref.ref(obj)
assert r() is obj
assert weakref.getweakrefcount(obj) == 1
assert weakref.getweakrefs(obj) == [r]
del obj
gc.collect()
assert r() is None
assert weakref.getweakrefcount(C()) == 0
assert weakref.getweakrefs(C()) == []

# Test weakref.ref(obj, callback)
class C: pass
obj = C()
called = []
def callback(arg):
    called.append(arg)
r = weakref.ref(obj, callback)
assert r() is obj
assert weakref.getweakrefcount(obj) == 1
assert weakref.getweakrefs(obj) == [r]
del obj
gc.collect()
assert r() is None
assert called == [C]
assert weakref.getweakrefcount(C()) == 0
assert weakref.getweakrefs(C()) == []

# Test weakref.proxy(obj)
class C: pass
