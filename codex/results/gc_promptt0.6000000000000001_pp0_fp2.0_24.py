import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C:
    pass

c = C()
c.attr = c
del c
gc.collect()
# Test __del__
class C:
    def __del__(self):
        pass

c = C()
c.attr = c
c.attr2 = weakref.ref(c)
del c
gc.collect()
# Test gc.collect() again
class C:
    pass

c = C()
c.attr = c
del c
gc.collect()
# Test __del__ again
class C:
    def __del__(self):
        pass

c = C()
c.attr = c
c.attr2 = weakref.ref(c)
del c
gc.collect()
