import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() doesn't clear all weakrefs to reachable objects.
class A:
    pass
def callback(wr):
    print "callback"
    print wr()
a = A()
wr = weakref.ref(a, callback)
print wr()
del a
gc.collect()
print wr()

# Test gc.collect() doesn't clear all weakrefs to unreachable objects.
def callback(wr):
    pass
a = A()
wr = weakref.ref(a, callback)
print wr()
del a
gc.collect()
print wr()
