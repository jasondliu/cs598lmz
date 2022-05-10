import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before the weakref callback is invoked.
# This used to crash because the weakref callback was invoked
# while the garbage was being collected.
#
# This test is kind of bogus because it relies on the garbage
# collector being run at a specific time.  It's not clear that
# this is something we should try to test.
def callback(obj):
    print 'callback'
    gc.collect()

class C:
    pass

c = C()
w = weakref.ref(c, callback)
del c
gc.collect()
print 'done'

# Make sure that a weakref callback is invoked when the object
# is part of a reference cycle.

def callback(obj):
    print 'callback'
    global called
    called = 1

class C:
    pass

c = C()
c.x = c
w = weakref.ref(c, callback)
del c
gc.collect()
assert called
print 'done'

# Make sure that a weakref callback is invoked when the object
# is part of a reference cycle that also contains a class.
