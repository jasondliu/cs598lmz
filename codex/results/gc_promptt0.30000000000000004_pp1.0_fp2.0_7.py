import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is intended to be run by a test driver which sets
# environment variables to control the test.
#
# The following environment variables are used:
#
#   GC_OPTS:  options to pass to gc.set_debug()
#   GC_DEBUG: debug flags to pass to gc.set_debug()
#
# The following environment variables are optional:
#
#   GC_DUMP: if set, dump the garbage collector state after each
#            collection
#   GC_VERBOSE: if set, print the garbage collector state after each
#               collection
#   GC_LEAK: if set, print a message when a test leaks objects
#   GC_STATS: if set, print a message with statistics after each
#             collection
#   GC_RUNS: if set, the number of times to repeat the test
#
# The following environment variables are used by the test driver
# to report the results of the test:
#
#   GC_COUNT: the number of objects collected
#   GC_FINALIZERS: the number of objects with finalizers

