import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
gc.collect()
# Check that weakrefs are not collected
assert gc.collect() == 0
# Check that weakrefs are not collected
assert gc.collect() == 0
# Check that weakrefs are not collected
assert gc.collect() == 0
# Check that weakrefs are not collected
assert gc.collect() == 0
# Check that weakrefs are not collected
assert gc.collect() == 0
# Check that weakrefs are not collected
assert gc.collect() == 0
# Check that weakrefs are not collected
assert gc.collect() == 0
# Check that weakrefs are not collected
assert gc.collect() == 0
# Check that weakrefs are not collected
assert gc.collect() == 0
# Check that weakrefs are collected
assert gc.collect() == 2
# Check that weakrefs are collected
assert gc.collect() == 0
# Check that weakrefs are collected
assert gc.collect() == 0
# Check that weakrefs are collected
assert gc.collect() == 0
#
