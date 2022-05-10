import weakref
# Test weakref.ref()
import weakref
import gc

class C(object):
    pass

o = C()
r = weakref.ref(o)

print r
print r()

o2 = C()
r2 = weakref.ref(o2)

print r2
print r2()

del o2
gc.collect()

print r2
print r2()

del o
gc.collect()

print r
print r()

# Test weakref.proxy()
import weakref
import gc

class C(object):
    pass

o = C()
p = weakref.proxy(o)

print p
print p.x

o.x = 1
print p.x

o2 = C()
p2 = weakref.proxy(o2)

print p2
print p2.x

o2.x = 1
print p2.x

del o2
gc.collect()

print p2
print p2.x

del o
gc.collect()

print p
print p.
