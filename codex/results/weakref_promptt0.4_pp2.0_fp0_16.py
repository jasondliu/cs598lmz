import weakref
# Test weakref.ref()
import gc

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
a = None
print(r)
gc.collect()
print(r)

# Test weakref.proxy()
a = A()
r = weakref.proxy(a)
print(r)
a = None
print(r)
gc.collect()
print(r)

# Test weakref.getweakrefcount()
a = A()
print(weakref.getweakrefcount(a))
r = weakref.ref(a)
print(weakref.getweakrefcount(a))
r = None
print(weakref.getweakrefcount(a))
a = None
gc.collect()
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs()
a = A()
print(weakref.getweakrefs(a))
r = weakref.ref(a)
print(weakref.getweakrefs(a))
r = None
print(weakref
