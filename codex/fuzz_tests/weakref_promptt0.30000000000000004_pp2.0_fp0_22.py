import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(o)

o2 = r()
print(o2)
print(o is o2)

o = None
print(r())

r = None
print(o2)

o2 = None
print(r)

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)
print(p.x)

o.x = 42
print(p.x)

o = None
print(p.x)

p = None
print(o)

# Test weakref.getweakrefcount()

class C:
    pass

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

p = weakref.proxy(o)
print(weakref.get
