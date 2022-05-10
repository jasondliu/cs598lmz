import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a class with a __del__ method and a
# weakref to that instance.

# Use the sample class from bug #1320700
class C(object):
    def __del__(self):
        print 'deleting', self

c = C()
w = weakref.ref(c)
print w()
print w() is None
del c
print w() is None
gc.collect()
print w() is None
gc.collect()
print w() is None
