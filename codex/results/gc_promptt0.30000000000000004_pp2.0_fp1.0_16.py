import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is not exhaustive.  It is meant to be extended as bugs are found.
#
# The tests are run twice, once with the Python debug build and once with
# the Python release build.  The Python debug build turns on extra sanity
# checks inside the Python interpreter.  The Python release build should be
# tested because it's what most users use.
#
# The tests are run in both verbose mode and quiet mode.  The verbose mode
# is useful for debugging a single test.  The quiet mode is useful for
# running the full test suite.

import gc, weakref
import sys

# A list of weakrefs to all objects created.  These are cleared by
# clear_objects().
all_objects = []

# A list of weakrefs to objects that should be collectable.  These are
# cleared by clear_objects().
collectable_objects = []

# A list of weakrefs to objects that should be uncollectable.  These are
# cleared by clear_objects().
uncollectable_objects = []

# A list of weakrefs to
