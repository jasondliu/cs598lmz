import weakref
# Test weakref.ref()
ref = weakref.ref(42)
assert ref() == 42
# Test weakref.proxy()
obj = []
proxy = weakref.proxy(obj)
assert proxy is obj
assert not isinstance(proxy, weakref.ProxyType)
# Test weakref.getweakrefs()
obj = []
r1 = weakref.ref(obj)
r2 = weakref.ref(obj)
r3 = weakref.ref(42)
refs = weakref.getweakrefs(obj)
assert len(refs) == 2
assert r1 in refs
assert r2 in refs
assert r3 not in refs
# Test weakref.getweakrefcount()
obj = []
r1 = weakref.ref(obj)
r2 = weakref.ref(obj)
r3 = weakref.ref(42)
assert weakref.getweakrefcount(obj) == 2
assert weakref.getweakrefcount(42) == 1
# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
obj = []
d[
