import weakref
# Test weakref.ref()
class C:
    pass
o = C()
r = weakref.ref(o)
print(r)
print(r())

# Test weakref.proxy()
o2 = C()
p = weakref.proxy(o2)
print(p)

# Test weakref.getweakrefcount()
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()
print(weakref.getweakrefs(o))

# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
o3 = C()
d[o3] = 1
print(d[o3])
print(d)
del o3
print(d)

# Test weakref.WeakValueDictionary
d2 = weakref.WeakValueDictionary()
o4 = C()
d2[1] = o4
print(d2[1])
print(d2)
del o4
print(d2)

# Test weakref.WeakSet
s = weakref.WeakSet()
o5
