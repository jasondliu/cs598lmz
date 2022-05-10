import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test should be run with the Python test suite, not on its own.
# It is listed in Lib/test/test_gc.py.
#
# The test verifies that gc.collect() collects all collectable objects.
# It also verifies that gc.garbage contains only truly uncollectable
# objects (i.e. objects that the collector found to be unreachable but
# could not collect because they had a __del__ method).
#
# The test works by creating a bunch of objects and deleting references
# to them from the global namespace dict.  Then gc.collect() is called
# and it verifies that all objects have been collected, and that the
# list of uncollectable objects is empty.
#
# The test is not foolproof.  It may fail if the collector is not able
# to collect some objects that the test assumed would be collectable.
# In this case the test prints a warning message.  The test may also
# fail if the collector finds some objects to be uncollectable that
# the test assumed would be collectable.  In this case the test prints

