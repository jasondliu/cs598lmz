import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = [object()]
wref = weakref.ref(a)
a = None
assert wref() is None
gc.collect() # Shouldn't collect here
b = [object()]
wref = weakref.ref(b)
b = None
assert wref() is None
gc.collect() # Should collect here

# Test gc._collect()
a = [object()]
wref = weakref.ref(a)
a = None
assert wref() is None
gc._collect() # Should collect here
b = [object()]
wref = weakref.ref(b)
b = None
assert wref() is None
gc._collect() # Should collect here
