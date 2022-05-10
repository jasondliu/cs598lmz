import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(1) with weakrefs on objects that are
# part of cyclic trash.  The purpose of the test is to
# verify that the call to gc.collect(1) does collect
# the referenced object.  Without the patch for issue
# #1516959 gc.collect(1) would not collect them.
class A:
    pass
def callback(wr):
    print "dead"

a = A()
b = A()
wr = weakref.ref(a, callback)
a.b = b
b.a = a
del a, b
for i in range(3):
    collected = gc.collect(1)
    if wr() is None:
        break
    assert collected == 1
    assert wr() is not None

del wr
collected = gc.collect(1)
assert collected == 1
print 'done'
