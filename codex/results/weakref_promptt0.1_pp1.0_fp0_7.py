import weakref
# Test weakref.ref()
import gc

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2)

print(r2)
print(r2())

del o2
print(gc.collect())
print(r2())

# Test weakref.proxy()
import weakref

class C:
    pass

o = C()
p = weakref.proxy(o)

print(p)

o2 = C()
p2 = weakref.proxy(o2)

print(p2)

del o2
print(p2)

# Test weakref.getweakrefcount()
import weakref

class C:
    pass

o = C()
d = weakref.WeakValueDictionary()
d['primary'] = o
r = weakref.ref(o)

print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

