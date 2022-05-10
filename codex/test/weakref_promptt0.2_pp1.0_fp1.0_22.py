import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
assert p is o

# Test weakref.getweakrefcount()

o = C()
assert weakref.getweakrefcount(o) == 0
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1

# Test weakref.getweakrefs()

o = C()
assert weakref.getweakrefs(o) == []
r = weakref.ref(o)
assert weakref.getweakrefs(o) == [r]

# Test weakref.finalize()

o = C()
l = []
def callback(wr):
    l.append(wr)
weakref.finalize(o, callback)
del o
assert l == [weakref.ref(l[0]())]

# Test weakref.WeakKeyDictionary

d = weak
