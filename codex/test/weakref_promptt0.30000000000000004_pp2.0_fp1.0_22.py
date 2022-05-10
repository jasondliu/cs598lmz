import weakref
# Test weakref.ref() and weakref.proxy()

import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(r(), p)

o2 = r()
o3 = p

print(o2 is o, o3 is o)

del o

print(r(), p)

o = C()

print(r(), p)

print(r() is o, p is o)

del o

print(r(), p)

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

del r

print(weakref.getweakrefcount(o))

del p

