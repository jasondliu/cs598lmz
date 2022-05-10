import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before __del__ is called.
class C(object):
    def __del__(self):
        print 'del'
gc.collect()
print '0 objects before creating a cycle'
c = C()
c.x = c
print '1 object for a cycle:', len(gc.garbage)
del c
print '0 objects after deletion of the cycle'
c = C()
c.x = c
wr = weakref.ref(c)
print '1 object after collecting, and a weakref'
gc.collect()
print '1 object after collecting, 1 more when weakref dies:'
del wr
gc.collect()
del c
gc.collect()

# Test gc.collect() after __del__ is called.
print
print "Test gc.collect() after __del__ is called."

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

class D(object):
    def __del__(self):
        print 'del'
d = D()
d.x = d
del d

gc.collect()
print
print "Test
