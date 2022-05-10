import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('callback'))
print(r2)
print(r2())

del o2
print(r2())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)
print(p.__class__)

o2 = C()
p2 = weakref.proxy(o2, lambda x: print('callback'))
print(p2)
print(p2.__class__)

del o2
print(p2)

# Test weakref.getweakrefcount()

o = C()
r = weakref.ref(o)
print(weakref.getweakrefcount(o))

o2 = C()
r2 = weakref.ref(o2)
print(weakref.getweakrefcount(o2))

#
