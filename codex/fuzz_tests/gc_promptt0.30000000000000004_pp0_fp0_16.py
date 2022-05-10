import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is designed to test the correctness of the garbage collector
# and the weakref module.  It is not designed to test the efficiency of
# the garbage collector.
#
# The test consists of a number of phases.  Each phase creates a bunch
# of objects and then collects them.  The objects created in each phase
# are different, and the phases are designed to test different features
# of the garbage collector.  The phases are run with and without the
# garbage collector enabled.  The phases are run in a random order to
# try to uncover any dependencies between the phases.
#
# The phases are:
#
#   1.  Create a bunch of old-style classes and instances.
#   2.  Create a bunch of new-style classes and instances.
#   3.  Create a bunch of cycles of old-style classes and instances.
#   4.  Create a bunch of cycles of new-style classes and instances.
#   5.  Create a bunch of cycles of old-style classes and instances
#       with __del__ methods that create new cycles.
#   6.  Create a bunch
