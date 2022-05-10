import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on objects with a weakrefable finalizer

class X(object):
    def __init__(self, id):
        self.id = id
        weakref.finalize(self, self.finalize, id)
    def __del__(self):
        pass
    def finalize(self, id):
        print "finalizing %d" % id

print "creating objects"
for i in range(100):
    X(i)
print "collecting"
n = gc.collect()
print "collected", n

# A special case: a class whose instances are weakrefable,
# but whose instances are not.
class W(object):
    def __del__(self):
        print "deleting W"

w = W()
wr = weakref.ref(w)
print "deleting w"
del w
print "collecting"
n = gc.collect()
print "collected", n
