import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations on a regrtest.py run.

import sys, os

# Number of cycles needed to trigger the uncollectable cycle.
# Without the referen
