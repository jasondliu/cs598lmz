import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

gc.collect()

def test_callback(object):
    print "CALLBACK", object

class A(object):
    pass

w = weakref.ref(A(), test_callback)
print w
del w
gc.collect()
print "OK"
