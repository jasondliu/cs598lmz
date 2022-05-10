import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and gc.garbage
a = []
b = [a]
c = [a, b]
a.append(b)
a.append(c)
del a, b, c
gc.collect()
print(gc.garbage)
# gc.garbage contains the objects that were resurrected by gc.collect()
class C(object):
    pass
c = C()
# create a cycle through a weakref
w = weakref.ref(c)
c.x = w
del c
# the weakref is still around
print(gc.get_referrers(w))
gc.collect()
# but the cycle is gone
print(gc.garbage)

# For more information, see the documentation of the gc module.
