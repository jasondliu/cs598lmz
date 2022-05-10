import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.callbacks
#
# Note: this test is designed to be run repeatedly by make test.py.  Each
# invocation may run in a different memory configuration, so the test has to
# work in whatever situation it encounters.
#
# Write the test in such a way that it can be run repeatedly.  The
# test will be run in various configurations of gc flags and thresholds,
# and will be run both with and without a debug allocator.
#
# When modifying this test, make sure you aren't assuming that there
# will be (or won't be) a debug allocator.  It would be nice if
# this test could be used to verify that the debug allocator works
# when it is in use, but the test shouldn't fail if it isn't in use
# (as it always will be in a release build).
#
# XXX Sometimes this test fails with an AttributeError or similar
# exception.  I think this is because a callback function is called
# and can't find objects that it expects to find.  This may
# indicate that gc.collect() didn't collect everything that it should

