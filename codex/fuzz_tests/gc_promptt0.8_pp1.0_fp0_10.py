import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class A:
    pass

def callback(wr):
    class B:
        pass
    B.wr = wr
    B.attr = 42
    return B.attr

x = A()
x.callback = lambda: callback(weakref.ref(x))
a = x.callback()
del x, A
gc.collect()
gc.collect()

# Check that the object and the weakref are still tracked, but not referenced.
gc.collect()
print "OK"
