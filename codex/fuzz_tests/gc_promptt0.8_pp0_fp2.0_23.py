import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs

class X:
    pass

class Y(X):
    pass

r = weakref.ref(X())
r1 = weakref.ref(X())
r2 = weakref.ref(Y())

# This next line will cause a blocking gc.collect()
del r

print gc.collect() # prints 2
print gc.collect() # prints 0
print gc.collect() # prints 0
# Test for gc.DEBUG_SAVEALL

print gc.get_debug()

gc.set_debug(gc.DEBUG_SAVEALL)
print gc.get_debug()

# This next line will cause a blocking gc.collect()
del r1

print gc.collect() # prints 1
print gc.collect() # prints 0
print gc.get_debug()

gc.set_debug(0)
print gc.get_debug()
class MyList(list):
    pass

gc.set_debug(gc.DEBUG_STATS)
lst = []
for i in range
