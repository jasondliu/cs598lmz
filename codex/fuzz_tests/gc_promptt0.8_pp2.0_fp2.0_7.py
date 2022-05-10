import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and gc.garbage
class A:
    def __del__(self):
        print("A.__del__")
        del self.attr
class B:
    def __del__(self):
        print("B.__del__")
        del self.attr
gc.collect()
print("Collecting...")
gc.collect()
a = A()
a.attr = weakref.ref(a)
b = B()
b.attr = weakref.ref(b)
a = b = None
gc.collect()
print("Collecting...")
gc.collect()
