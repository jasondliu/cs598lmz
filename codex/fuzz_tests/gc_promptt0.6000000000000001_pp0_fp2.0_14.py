import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class X(object):
    pass

class Y(object):
    pass

a = X()
b = Y()
a_ref = weakref.ref(a)
b_ref = weakref.ref(b)
a.b = b
b.a = a

print gc.collect()
print len(gc.garbage)
print gc.collect()
print len(gc.garbage)

del a
del b

print gc.collect()
print len(gc.garbage)
print gc.collect()
print len(gc.garbage)
