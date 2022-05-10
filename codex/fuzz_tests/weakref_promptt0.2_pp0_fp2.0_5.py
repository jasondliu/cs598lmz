import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f

# Test weakref.proxy()

p = weakref.proxy(f)
assert p is f

# Test weakref.getweakrefcount()

assert weakref.getweakrefcount(f) == 1

# Test weakref.getweakrefs()

assert weakref.getweakrefs(f) == [r]

# Test weakref.finalize()

class Foo:
    pass

def callback(wr):
    print("callback called")

f = Foo()
wr = weakref.finalize(f, callback)
assert wr.alive
del f
gc.collect()
assert not wr.alive

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
f = Foo()
d[f] = 1
assert d[f] == 1
del f
gc.collect()
assert len(d) == 0

# Test weakref.WeakValueDictionary

