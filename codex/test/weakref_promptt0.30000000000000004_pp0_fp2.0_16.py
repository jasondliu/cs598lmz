import weakref
# Test weakref.ref() and weakref.proxy()

import weakref
import gc

class C:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(r(), p)
print(r() is p)
print(r() is o)

o2 = r()
o3 = p
print(o2 is o3)

del o
gc.collect()

print(r() is o2)
print(r() is o3)

print(r() is None)
print(p is None)

# Test weakref.getweakrefcount()

import weakref

class C:
    pass

o = C()
d = weakref.WeakKeyDictionary()
d[o] = 1

print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

import weakref

class C:
    pass

o = C()
d = weakref.WeakKeyDictionary()
d[o] = 1

