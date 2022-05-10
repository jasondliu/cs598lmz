import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is not exhaustive, but it does exercise the
# collect() API and some important internal details.
#
# The tests are run twice, first with a fast malloc implementation
# (just to exercise the code), and then with a debug malloc that
# verifies proper usage.

import gc, weakref

# Test gc.collect() with a fast malloc
gc.set_debug(gc.DEBUG_STATS)
gc.collect()

# Test gc.collect() with a debug malloc
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.collect()

# Test gc.collect() with a debug malloc and collectable objects
gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_LEAK)
gc.collect()

# Test gc.collect() with a debug malloc and uncollectable objects
gc.set_debug(gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_LEAK)
gc.collect()

# Test gc.collect() with a
