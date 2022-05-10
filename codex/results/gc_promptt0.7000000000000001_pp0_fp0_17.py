import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
print 'Expect 0:', gc.collect()
print 'Expect 0:', gc.collect()

# Create a cycle.
class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a
# Test that collect finds it.
print 'Expect 0:', gc.collect()

# Test that a callbacks are called.

def callback0(obj):
    print 'callback 0'
def callback1(obj):
    print 'callback 1'
gc.register_callback(callback0)
gc.register_callback(callback1)
gc.collect()

# Test that uncollectable objects are collected.
class B:
    pass
b = B()
b.b = B()
# Test that uncollectable objects are not collected.
b.b.b = b
del b
gc.collect()

# Test that a weakref callback is called.

d = {}
def callback2(reference):
    print 'callback 2'
weakref.ref(d, callback2)
del d

