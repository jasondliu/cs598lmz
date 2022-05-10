import weakref
# Test weakref.ref()

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

o = o2 = None
print(r())
print(r2())

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)

o = o2 = None

# Test weakref.getweakrefcount()

class C:
    pass

o = C()
r = weakref.ref(o)
print(weakref.getweakrefcount(o))

o2 = C()
r2 = weakref.ref(o2)
print(weakref.getweakrefcount(o2))

o = o2 = None

# Test weakref.getweak
