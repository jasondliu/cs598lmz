import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# The test consists of a number of phases.  Each phase tests a different
# aspect of the garbage collector.  All phases are run twice: once with
# garbage collection enabled, and once with it disabled.  The first run
# tests the garbage collector itself, and the second run tests that
# garbage collection doesn't break things that are supposed to work even
# without garbage collection.
#
# Each phase is run with garbage collection enabled by calling the
# run_phase() function with the phase number.  This function is also
# responsible for printing out the phase number before starting the phase.
#
# Each phase is run with garbage collection disabled by calling the
# run_phase() function with the phase number negated.
#
# The test is run with a variety of different garbage collection thresholds,
# in order to make sure that the garbage collector doesn't break when the
# thresholds change.

# Print the test phase number, and run the test with garbage collection
# enabled and disabled.
def run_phase(phase):
    print "phase", phase
    if phase > 0:
        gc.enable()
    else:
