import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect (without using it) with a different debug value
previousDebugValue = gc.get_debug()
gc.set_debug(previousDebugValue - 1)
check(gc.get_debug() == previousDebugValue - 1)
check(gc.collect(2) == 0)
check(gc.collect(1) == 0)
check(gc.collect(0) == 0)
check(gc.collect(-1) == 0)
check(gc.get_debug() == previousDebugValue - 1)
gc.set_debug(previousDebugValue)
check(gc.collect(2) == 0)
check(gc.collect(1) == 0)
check(gc.collect(0) == 0)
check(gc.collect(-1) == 0)
check(gc.get_debug() == previousDebugValue)

# Test weakref construction
class C:
    pass

c = C()
w = weakref.ref(c)
check(w() is c)

class P(object):
    pass

p = P()
check(p is weakref.ref(
