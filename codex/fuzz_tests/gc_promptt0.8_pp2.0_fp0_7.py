import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage.
#
# When run in verbose mode, this script prints one line for each object
# collected or examined.  The first two numbers on each line are the object's
# address and the address of its refcounts.  For collected objects, the third
# number is zero; for examined objects, it gives the object's refcount.
#
# GC runs are triggered by creating cycles or by reaching a threshold number
# of allocated objects.  The script starts by allocating 524 objects.  This
# is enough to trigger a full collection.  In verbose mode, it prints a
# line @ at this point.  When the full collection has completed, it prints a
# line #.  After that, it doubles the number of allocated objects each time,
# until the number reaches 2,097,152, at which point it stops.  In the
# between-collections intervals, it creates cycles of various sizes and
# collects again, printing * lines to mark these runs.

n = 512
allocated = 0
collected = []
uncollectable = []

# Test a list of objects.
