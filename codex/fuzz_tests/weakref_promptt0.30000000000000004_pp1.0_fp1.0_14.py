import weakref
# Test weakref.ref()
import weakref

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
print(r2())

# Test weakref.proxy()
import weakref

class C:
    pass

o = C()
p = weakref.proxy(o)

print(p)
print(p.foo)

o2 = C()
p2 = weakref.proxy(o2)

print(p2)
print(p2.foo)

del o2
print(p2.foo)

# Test weakref.getweakrefcount()
import weakref

class C:
    pass

o = C()

print(weakref.getweakrefcount(o))

r = weakref.ref(o)

print(weakref.getweakrefcount(o))

o2 = C
