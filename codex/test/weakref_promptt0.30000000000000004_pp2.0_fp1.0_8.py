import weakref
# Test weakref.ref()
class C:
    pass
o = C()
r = weakref.ref(o)
print(r)
print(r())

# Test weakref.proxy()
o = C()
p = weakref.proxy(o)
print(p)

# Test weakref.getweakrefcount()
o = C()
d = weakref.WeakValueDictionary()
d['primary'] = o
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()
o = C()
d = weakref.WeakValueDictionary()
d['primary'] = o
print(weakref.getweakrefs(o))

# Test weakref.finalize()
o = C()
f = weakref.finalize(o, lambda o: print("finalized"))
print(f.alive)
del o
print(f.alive)

# Test weakref.WeakKeyDictionary()
d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
print(d[o])
