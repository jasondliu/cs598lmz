import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
# gc.collect()

class C(object):
    def __init__(self, arg1):
        self.arg1 = arg1

c = C(1)
w = weakref.ref(c)
print 'w:', w
print 'c:', c
print 'w():', w()
print
c = None
print gc.collect()
print 'w():', w()
