import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r())

# Test weakref.ref(obj, callback)

class C:
    pass

o = C()
r = weakref.ref(o, lambda r: print('callback', r))
print(r)
print(r())

del o
print(r())

# Test weakref.getweakrefcount(obj)

class C:
    pass

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

r2 = weakref.ref(o)
print(weakref.getweakrefcount(o))

del r
print(weakref.getweakrefcount(o))

del r2
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs(obj)

class C:
