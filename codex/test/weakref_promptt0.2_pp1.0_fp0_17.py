import weakref
# Test weakref.ref()

import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r())

# Test weakref.proxy()

import weakref

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)
print(p.__class__)

del o
try:
    print(p)
except ReferenceError:
    print('ReferenceError')

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
print(weakref.getweakrefcount(o))

#
