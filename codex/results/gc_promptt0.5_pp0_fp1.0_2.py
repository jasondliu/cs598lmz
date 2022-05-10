import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs

class Test:
    pass

t = Test()
w = weakref.ref(t)
del t
gc.collect()
assert w() is None
gc.collect()

# Test gc.collect with weakrefs in a cycle

class Test:
    pass

t = Test()
w = weakref.ref(t)
t.w = w
del t
gc.collect()
assert w() is None
gc.collect()

# Test gc.collect with a weakref to an instance

class Test:
    pass

t = Test()
w = weakref.ref(t)
del t
gc.collect()
assert w() is None
gc.collect()

# Test gc.collect with weakrefs in a cycle to an instance

class Test:
    pass

t = Test()
w = weakref.ref(t)
t.w = w
del t
gc.collect()
assert w() is None
gc.collect()

# Test gc.collect with a weakref to a class

class Test
