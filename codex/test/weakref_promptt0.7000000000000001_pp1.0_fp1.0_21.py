import weakref
# Test weakref.ref:
r = weakref.ref(old_object)
r() is old_object
r() is not None
