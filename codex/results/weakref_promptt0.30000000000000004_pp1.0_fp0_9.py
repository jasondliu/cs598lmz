import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)
print(r() is None)

# Test weakref.proxy(obj)

p = weakref.proxy(o)
print(p)
print(p is o)
print(p is None)

# Test weakref.getweakrefcount(obj)

print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs(obj)

print(weakref.getweakrefs(o))

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
d[o] = 1
print(d[o])
print(d)
del o
print(d)

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
d[1] = o
print(d[1])
print(d)
del o
print(d)

# Test weak
