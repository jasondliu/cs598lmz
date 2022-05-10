import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs

class A:
    pass

class B(A):
    pass

a = A()
b = B()
weakref.ref(a)
weakref.ref(b)

gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash
gc.collect()

# This should not crash

