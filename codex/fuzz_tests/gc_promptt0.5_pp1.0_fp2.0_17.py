import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class C:
    pass

o = C()
r = weakref.ref(o)
print r() is o
del o
gc.collect()
print r()
# Test weakref.proxy()
class C:
    pass

o = C()
p = weakref.proxy(o)
print p is o
del o
gc.collect()
try:
    print p
except ReferenceError, err:
    print err
# Test gc.get_referrers()
class C:
    pass

o = C()
r = weakref.ref(o)
print r() is o
print gc.get_referrers(o) == [o]
del o
gc.collect()
print gc.get_referrers(r) == [r]
# Test gc.get_referrers()
class C:
    pass

o = C()
r = weakref.ref(o)
print r() is o
print gc.get_referrers(o) == [o]
del o

