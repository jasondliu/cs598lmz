import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test checks that gc.collect() works on objects with a
# __del__ method.

class A:
    def __del__(self):
        self.x = 1

a = A()
a.x = 2

weakref.ref(a)

gc.collect()

if a.x != 2:
    raise RuntimeError("a.x != 2")
