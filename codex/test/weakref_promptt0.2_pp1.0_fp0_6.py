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

o = C()
r = weakref.ref(o)
print(r)
print(r())

o = None
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
print(p.foo)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)
print(p2.foo)

o = C()
p = weakref.proxy(o)
print(p)
print(p.foo)

o = None
gc.collect()
print(p)
print(p.foo)

