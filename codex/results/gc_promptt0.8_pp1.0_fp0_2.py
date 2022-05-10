import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when a reachable object contains a weakref to a reachable but uncollectable
# object, (but not the other way around)
class A:
    pass

a = A()

def callback(w):
    print('callback', w)

wr = weakref.ref(a, callback)

gc.collect()
gc.collect()
# Test gc.collect() when a reachable object contains a weakref to a reachable but uncollectable
# object, (but the other way around)
class A:
    pass

a = A()

def callback(w):
    print('callback', w)

a.wr = weakref.ref(a, callback)

gc.collect()
gc.collect()
# Test gc.collect() when a reachable object contains a weakref to a reachable but uncollectable
# object, (but not the other way around)
class A:
    pass

a = A()

def callback(w):
    print('callback', w)

wr = weakref.ref(a, callback)

gc.collect
