import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs.
#
# This tests the case where a weakref is the only reference to an object,
# and the object has a __del__ method.

class C:
    def __del__(self):
        #print "deleting", self
        pass

def callback(w):
    global n_callback_called
    n_callback_called += 1

n_callback_called = 0

def f():
    o = C()
    o.wr = weakref.ref(o, callback)
    #print "refcount before =", sys.getrefcount(o)
    gc.collect()
    #print "refcount after =", sys.getrefcount(o)
    #print "callback called", n_callback_called
    if n_callback_called != 1:
        raise TestFailed, "callback called %d times" % n_callback_called

f()
# Test that gc.collect() calls the __del__ method on objects whose
# refcount goes to zero as a result of the collection.

def f():
    class C
