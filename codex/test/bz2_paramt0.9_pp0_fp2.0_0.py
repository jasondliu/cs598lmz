from bz2 import BZ2Decompressor
BZ2Decompressor()

# Verify that GC enum instances can be accessed as module attributes
import gc
gc.DEBUG_STATS
gc.DEBUG_LEAK
gc.DEBUG_COLLECTABLE
gc.DEBUG_UNCOLLECTABLE

# Verify that resource module enum types can be accessed as module attributes
import resource
resource.RLIMIT_AS
resource.RLIMIT_CORE
resource.RLIMIT_CPU
resource.RLIMIT_DATA
resource.RLIM_INFINITY
