import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() vs. __del__ on uncollectable objects.

class C:
    def __del__(self):
        print "del"

c = C()
w = weakref.ref(c)
c.x = c
c.y = c
c.z = c
del c

print gc.collect()
print w()
print w()
print w()
