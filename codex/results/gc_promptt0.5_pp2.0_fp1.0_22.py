import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs to objects with a finalizer:
#
#   - check that the finalizer is called
#   - check that the finalizer is called only once
#   - check that the finalizer is called before the object is freed
#   - check that the finalizer can create a new reference to the object
#   - check that the finalizer can create a new reference to the object
#     and then delete the reference
#   - check that the finalizer can create a new reference to the object,
#     delete the reference, and then create a new reference to the object
#     again
#   - check that the finalizer can create a new reference to the object,
#     delete the reference, create a new reference to the object, and then
#     delete the reference again
#   - check that the finalizer can create a new reference to the object,
#     delete the reference, create a new reference to the object, delete
#     the reference, create a new reference to the object, and then delete
#     the reference again
#   - check that the finalizer can create a new reference to the object,
#     delete
