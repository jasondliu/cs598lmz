import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().

___assertEqual(gc.collect(), 0)

class C:
    pass

c1 = C()
c2 = C()
c3 = C()
c4 = C()
l = [weakref.ref(C()), weakref.ref(c3), weakref.ref(c4)]
# We expect l[0] to go away, because there are no more strong references to the C instance

___assertEqual(gc.collect(), 1)
___assertTrue(l[0]() is None)

# But c3 and c4 are kept around by weakrefs with tp_clear, so their refcounts stay > 0

___assertTrue(gc.collect() > 0)
___assertFalse(l[1]() is None)
___assertFalse(l[2]() is None)
___assertFalse(c3 is None)
___assertFalse(c4 is None)

# get_referents returns a list of all objects that can be reached from the argument object

class C:
    pass

obj = C()
selfref = [obj
