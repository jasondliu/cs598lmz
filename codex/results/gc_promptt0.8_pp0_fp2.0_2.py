import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(0)
gc.collect(0)
gc.collect(0)
gc.collect(0)
del gc.garbage[:]

# Unreachable
class A(object):
    def __del__(self):
        print "deleting"
a = A()
b = A()
b.x = a
a.x = b
del a,b

gc.collect(0)
gc.collect(0)
gc.collect(0)
gc.garbage

del gc.garbage[:]

# Reachable, but with a cycle
class A(object):
    def __del__(self):
        print "deleting"
a = A()
b = A()
b.x = a
a.x = b

import gc, weakref
gc.set_debug(gc.DEBUG_INSTANCES)
gc.collect(0)
gc.collect(0)
ref = weakref.ref(b)
ref
del a,b,ref
gc.garbage

# A cycle involving the magic set-state slot

