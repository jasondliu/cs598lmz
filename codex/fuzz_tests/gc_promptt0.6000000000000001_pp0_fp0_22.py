import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on a weakref callbacks.
# The callback should be called by gc.collect()
# if there is no other reference to the object
# (and the callback is reachable).
#
# This is also a regression test for SF bug #813338,
# where weakref callbacks were not called if they
# were reachable only through their argument.

class A:
    pass

class B:
    pass

class C(B):
    pass

# Create some objects:
#   a is a reachable instance of A
#   r is a weak reference to a
#   b is an unreachable instance of B
#   c is an unreachable instance of C
#   d is a weak reference to c
#   e is a weak reference to c
#   f is an unreachable instance of C
#   g is a weak reference to f
a = A()
r = weakref.ref(a)
b = B()
c = C()
d = weakref.ref(c, lambda w: print("called d"))
e = weakref.ref(c, lambda w:
