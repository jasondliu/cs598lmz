import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callable object.

# This calls the callable object at most once.
def callback(obj):
    print('callback({})'.format(obj))
    obj.callback = None

# This calls the callable object at most twice.
def callback2(obj):
    print('callback2({})'.format(obj))
    obj.callback2 = None

# This calls the callable object at most twice.
def callback3(obj):
    print('callback3({})'.format(obj))
    obj.callback3 = None

# This calls the callable object at most thrice.
def callback4(obj):
    print('callback4({})'.format(obj))
    obj.callback4 = None

class C(object):
    pass

c = C()
c.callback = weakref.ref(c, callback)
c.callback2 = weakref.ref(c, callback2)
c.callback3 = weakref.ref(c, callback3)
c.callback4 = weakref.ref(c, callback4)

print('collecting
