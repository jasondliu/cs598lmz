import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when tp_clear is not defined.
class X:
    def __del__(self):
        print "X.__del__()"

def foo(x):
    print "foo() gc_collect"
    gc.collect()

class Y:
    def __del__(self):
        print "Y.__del__()"

x = X()
w = weakref.ref(x, foo)
print x
del x
print w()
c = Y()
del c
print w()
# If a tp_clear method doesn't exist, the best the garbage collector can do
# is to clear the slot the weakref is stored in.
# X.__del__ should be called now.
