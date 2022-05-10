import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() doesn't crash recursively after a gc.collect()
gc.collect()

class LatentCycle:
    def __init__(self, next):
        self.next = next
    def __del__(self):
        self.next = None

a = LatentCycle(None)
a = LatentCycle(a)
# Now a and a.next are both part of a cycle that is collectable.
# If the finalizers run this will release the cycle and so the object will be
# uncollectable, but is not being tracked as such and hence the following
# call to collect() will enter an infinite loop (a.next and a will
# permanently remain collectable).
gc.collect()
