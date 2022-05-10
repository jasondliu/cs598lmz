import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() -> "Callbacks"

# No callback registered.

gc.collect()

# Callback registered, but no objects to call back on.

ob = weakref.ref(None)
gc.collect()

# Callback registered, but no reference cycles.

x = [1]
def func():
    print(x)
cb = weakref.finalize(None, func)
gc.collect()

# Callback registered, plus a reference cycle.

ob = []
ob.append(ob)
cb.atexit = ob = weakref.ref(ob, func)
gc.collect()

# Callback registered, reference cycle broken.

ob = []
ob.append(ob)
cb.atexit = ob = weakref.ref(ob, func)
ob = None
gc.collect()
# Test gc.collect() -> "Collect the uncollectable"

# Test: uncollectable lists.

lst = []
lst.append(lst)
lst1 = [0]
lst1.append(lst1)
lst
