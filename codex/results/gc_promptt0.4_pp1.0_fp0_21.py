import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref.ref

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
del a
gc.collect()
print(r)

# Test weakref.proxy

class B:
    pass

b = B()
p = weakref.proxy(b)
print(p)
del b
gc.collect()
print(p)

# Test weakref.getweakrefcount

a = A()
r = weakref.ref(a)
print(weakref.getweakrefcount(a))
del r
print(weakref.getweakrefcount(a))
del a

# Test weakref.getweakrefs

a = A()
r = weakref.ref(a)
print(weakref.getweakrefs(a))
del r
print(weakref.getweakrefs(a))
del a

# Test weakref.proxytype

print(weakref.proxytype)

# Test weakref.ReferenceType

print
