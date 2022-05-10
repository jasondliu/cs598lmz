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
print(o2 is o)
print(o2 == o)
print(o2 is p)
print(o2 == p)

o = None
print(r(), p)
print(r() is None)
print(r() == None)
print(r() is p)
print(r() == p)

print(p is None)
print(p == None)

# Test weakref.getweakrefcount()

import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(weakref.getweakrefcount(o))
print(weakref.getweakrefcount(r))
print(weakref.getweakrefcount(p))

# Test weakref.getweakrefs()

