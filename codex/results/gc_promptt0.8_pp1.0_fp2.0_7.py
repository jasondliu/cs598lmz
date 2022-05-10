import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect in different modes
for i in xrange(gc.get_count()):
    gc.collect(i)

# Create a bunch of objects that are collectable.
class Foo:
    pass
cls = Foo
cls_refs = []
for i in xrange(1000):
    cls_refs.append(weakref.ref(cls))
    cls = cls.__class__

# Verify that they're collectable.
gc.collect()
print 'Uncollectable classes:', [cls for cls in cls_refs if cls()]

gc.set_debug(0)

# Test cycles involving overriding __del__ methods.

class A:
    def __init__(self, i):
        self.i = int(i)
    def __repr__(self):
        return 'A(%s)' % self.i
    def __del__(self):
        print "Deleting", self
a1 = A(1)
a2 = A(2)
a1.c = a2
a2.
