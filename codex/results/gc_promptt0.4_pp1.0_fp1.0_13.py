import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C:
    def __del__(self):
        print 'del'

c = C()
c.a = c
del c
gc.collect()

# Test gc.collect()
class C:
    def __del__(self):
        print 'del'

c = C()
c.a = weakref.ref(c)
del c
gc.collect()

# Test gc.collect()
class C:
    def __del__(self):
        print 'del'

c = C()
c.a = weakref.ref(c)
c.b = c
del c
gc.collect()

# Test gc.collect()
class C:
    def __del__(self):
        print 'del'

c = C()
c.a = weakref.ref(c)
c.b = c
c.c = weakref.ref(c)
del c
gc.collect()

# Test gc.collect()
class C:
    def __del__(self):
        print 'del'

