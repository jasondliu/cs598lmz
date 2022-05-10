import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and weakref callbacks with
# objects in the collectable state.
# Also test that resurrecting objects works, and
# that the callbacks are still called.

def callback(ignore):
    print("called back")

# 10x10 array of tuples, with a callback on each tuple

weakrefs = []

for i in range(10):
    t = []
    for j in range(10):
        t.append((i*10 + j, weakref.ref(t, callback)))
    weakrefs.append(t)

# Remove references to the tuples, so they can be collected

del t
del i, j
gc.collect()
if weakref.getweakrefcount(weakrefs) != 1:
    print("error: getweakrefcount returned",
          weakref.getweakrefcount(weakrefs))

for t in weakrefs:
    for u in t:
        if u[1]() is not t:
            print("error: callback still holds a reference")

# Create several more tuples with callbacks, so

