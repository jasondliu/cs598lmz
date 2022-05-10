import weakref
# Test weakref.ref()
import gc

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
gc.collect()
print(r)
print(r())

# Test weakref.proxy()
import weakref

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)

del o
print(p)

# Test weakref.getweakrefcount()
import weakref

class C:
    pass

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

p = weakref.proxy(o)
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()
import weakref

class C:
    pass

o = C()
print(weakref.getweakrefs(o))

r = weakref.ref(o)

