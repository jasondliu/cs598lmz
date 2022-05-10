import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

class A:
    pass

def callback(wr):
    print "callback", wr()

def callback2(wr):
    print "callback2", wr()

def callback3(wr):
    print "callback3", wr()

def callback4(wr):
    print "callback4", wr()

a = A()
wr = weakref.ref(a, callback)
wr2 = weakref.ref(a, callback2)
wr3 = weakref.ref(a, callback3)
wr4 = weakref.ref(a, callback4)
print "before", wr(), wr2(), wr3(), wr4()
del a
gc.collect()
print "after", wr(), wr2(), wr3(), wr4()

# Before:
# callback <__main__.A instance at 0x00A1D1B0>
# callback2 <__main__.A instance at 0x00A1D1B0>
# callback3 <__main__.A instance at 0x00A1D1B0>
# callback4 <
