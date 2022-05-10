import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)
print(p is o)

# Test weakref.getweakrefcount()

o = C()
d = weakref.WeakKeyDictionary()
d[o] = 1
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

o = C()
d = weakref.WeakKeyDictionary()
d[o] = 1
l = weakref.getweakrefs(o)
print(l)

# Test weakref.finalize()

o = C()
f = weakref.finalize(o, lambda o: print("finalized"))
print(f.alive)
del o
print(f.alive)

# Test weakref.WeakSet

o = C()
s =
