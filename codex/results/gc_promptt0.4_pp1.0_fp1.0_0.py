import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs to objects with __del__ methods.

# The weakref callbacks are called before the object's __del__ method.

class C:
    def __init__(self):
        self.callback_called = False
        self.ref = weakref.ref(self, self.callback)

    def callback(self, wr):
        self.callback_called = True

    def __del__(self):
        print("__del__ called")

# Case 1:  The weakref callback is called before the __del__ method.

c = C()
c.ref()
del c
gc.collect()
print("callback called:", c.callback_called)

# Case 2:  The weakref callback is called before the __del__ method, but
# the object is not collected because it is still reachable from the
# weakref object.

c = C()
c.ref()
del c
gc.collect()
print("callback called:", c.callback_called)

# Case 3:  The weakref callback is called before the __del__ method, but
