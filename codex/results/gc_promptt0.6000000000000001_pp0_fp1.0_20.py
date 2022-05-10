import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

c = C()
wr = weakref.ref(c)

gc.collect()

#print "collecting", gc.collect()
#print "unreachable", [o for o in gc.garbage if o is c]
#print "weakref", wr()
#print "weak dict", wr() is c

# This used to fail with a reference count of 2, because the weakref
# kept a reference to the instance in its __call__ method.

#print "collecting", gc.collect()
#print "unreachable", [o for o in gc.garbage if o is c]
#print "weakref", wr()
#print "weak dict", wr() is c

#print "collecting", gc.collect()
#print "unreachable", [o for o in gc.garbage if o is c]
#print "weakref", wr()
#print "weak dict", wr() is c
