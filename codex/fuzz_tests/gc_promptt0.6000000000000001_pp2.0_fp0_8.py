import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before and after weakref.ref()
r = weakref.ref(gc.garbage[0])
gc.collect()
r()

# Test gc.collect() before and after weakref.ref()
# with a __del__ method
class A:
    def __del__(self):
        pass
r = weakref.ref(A())
gc.collect()
r()

# Test gc.collect() before and after weakref.proxy()
r = weakref.proxy(gc.garbage[0])
gc.collect()
r

# Test gc.collect() before and after weakref.proxy()
# with a __del__ method
class A:
    def __del__(self):
        pass
r = weakref.proxy(A())
gc.collect()
r


# Test gc.get_referrers()
a = []
b = [a]
c = [b]
d = [c]
gc.get_referrers(a) == [b]
gc.get_referrers(b) == [c]
gc
