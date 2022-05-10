import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when there's an uncollectable finalizer in a weak-refable instance.

class C:
    def __init__(self):
        self.wr = weakref.ref(self)

    def __del__(self):
        print("del")
        # The weak ref is still alive at this point.
        if self.wr() is not None:
            print("no")

c = C()
wr = weakref.ref(c)
c = None
gc.collect()
# If the weak ref is still alive, the object's finalizer has not run.
if wr() is None:
    print("ok")
else:
    print("no")
