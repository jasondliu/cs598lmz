import weakref
# Test weakref.ref()
import _weakref

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f
assert isinstance(r, _weakref.ReferenceType)

# Test weakref.proxy()
p = weakref.proxy(f)
assert p is f
assert isinstance(p, weakref.ProxyType)

# Test weakref.getweakrefcount()
assert weakref.getweakrefcount(f) == 2

# Test weakref.getweakrefs()
assert weakref.getweakrefs(f) == [r, p]

# Test weakref.finalize()

class FinalizeTest:
    def __init__(self):
        self.finalized = False
    def __del__(self):
        self.finalized = True

ft = FinalizeTest()
f = weakref.finalize(ft, lambda: None)
assert not ft.finalized
del ft
assert f.alive
f()
assert f.alive
import gc
gc.collect()
assert not f
