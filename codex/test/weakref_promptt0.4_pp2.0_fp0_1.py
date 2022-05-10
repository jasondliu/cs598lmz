import weakref
# Test weakref.ref()
class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o
assert r() is not None
assert r() is not None

# Test weakref.proxy()
p = weakref.proxy(o)
assert p is o
assert p is not None
assert p is not None

# Test weakref.getweakrefcount()
assert weakref.getweakrefcount(o) == 1

# Test weakref.getweakrefs()
assert weakref.getweakrefs(o) == [r]

# Test weakref.finalize()
class Finalize(object):
    def __init__(self, callback):
        self.callback = callback
    def __del__(self):
        self.callback()

