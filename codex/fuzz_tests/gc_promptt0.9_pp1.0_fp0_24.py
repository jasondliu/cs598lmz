import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after freeing up a finalized object.

def callback(*args):
    print("callback")
#    l.remove(wr)

class A:
    def __init__(self, callback):
        self.callback = callback
    def __del__(self):
        self.callback()

l = [A(callback) for i in range(10)]
l = [A(callback) for i in range(10)]
# We don't care about the list, just the individual objects.
del l
wr = weakref.ref(A(callback))
print("Removing (but keeping ref)", wr)
del wr.callback
del A.__del__
del A.__init__
del callback

gc.collect()
gc.collect()
print("Removing weakref")
# gc doesn't collect the weakref if its callback is alive.
del wr
gc.collect()
# wr is gone now, so the callback is deleted too.
gc.set_threshold(8)
# We have 3 unreachable objects left :
# - the class A
# - the function callback
# -
