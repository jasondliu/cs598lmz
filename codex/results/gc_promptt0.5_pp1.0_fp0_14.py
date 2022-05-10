import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    return weakref.ref(gc.collect())
r = f()
del f
gc.collect()
print(r())

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

class A:
    def __del__(self):
        print("deleted")

a = A()
a = None
gc.collect()

gc.set_debug(gc.DEBUG_STATS)
a = A()
a = None
gc.collect()

gc.set_debug(gc.DEBUG_LEAK)
a = A()
a = None
gc.collect()

gc.set_debug(0)

# Test gc.is_tracked()
class X:
    pass

x = X()
print(gc.is_tracked(x))
del x
gc.collect()
print(gc.is_tracked(X()))

# Test gc.get_referrers()
class Y:
    pass

y = Y()
print(gc.get_referrers(y))


