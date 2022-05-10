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

# Test weakref.WeakKeyDictionary()

d = weakref.WeakKeyDictionary()
d[f] = 1
assert d[f] == 1

# Test weakref.WeakValueDictionary()

d = weakref.WeakValueDictionary()
d[1] = f
assert d[1] is f

# Test weakref.finalize()

class Foo:
    pass

f = Foo()

def callback(wr):
    print("callback called")

wr = weakref.finalize(f, callback, f)
assert wr.alive

del f

