import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when __del__() is called from a weakref callback
# when the object has a finalizer.
class A:
    def __init__(self):
        self.wr = weakref.ref(self, lambda wr, self=self: self.finalize())
    def finalize(self):
        print("finalizing")
        # self.__del__ is already on the finalizer queue, so this
        # is redundant, but it's here to test that it doesn't crash.
        gc.collect()
        del self.wr
    def __del__(self):
        print("deleting")
        del self.wr

print("creating")
a = A()
print("collecting")
gc.collect()
print("done")
