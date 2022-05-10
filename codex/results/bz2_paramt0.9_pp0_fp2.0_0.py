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
resource.RLIM_SAVED_MAX
resource.RLIM_SAVED_CUR
resource.RLIMIT_FSIZE
resource.RLIMIT_LOCKS
resource.RLIMIT_MEMLOCK
resource.RLIMIT_NOFILE
resource.RLIMIT_NPROC
resource.RLIMIT_RSS
resource.RLIMIT_STACK
resource.RUSAGE_SELF
resource.RUSAGE_CHILDREN
resource.RUSAGE_BOTH
resource.RLIM_NLIMITS
resource.PRIO_PROCESS
resource.PRIO_PGRP
resource.PR
