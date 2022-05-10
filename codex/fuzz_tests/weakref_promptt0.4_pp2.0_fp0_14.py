import weakref
# Test weakref.ref()
r = weakref.ref(42)
assert r() == 42

# Test weakref.proxy()
p = weakref.proxy(42)
assert p == 42

# Test weakref.getweakrefcount()
assert weakref.getweakrefcount(42) == 1

# Test weakref.getweakrefs()
assert weakref.getweakrefs(42) == [r]

# Test weakref.finalize()
class Foo:
    pass

def callback():
    pass

f = Foo()
w = weakref.finalize(f, callback)
assert w.alive == True
del f
assert w.alive == False

# Test weakref.WeakKeyDictionary()
d = weakref.WeakKeyDictionary()
d[42] = 42
assert 42 in d
del 42
assert 42 not in d

# Test weakref.WeakValueDictionary()
d = weakref.WeakValueDictionary()
d[42] = 42
assert 42 in d
del 42
assert 42 not in d

# Test weakref.WeakSet
