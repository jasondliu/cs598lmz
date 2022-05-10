import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# The following test is based on the assumption that gc.collect()
# will collect all objects which are collectable.
#
# This is not true.  gc.collect() collects a *subset* of collectable
# objects.  There is no way to force it to collect all collectable
# objects.  I think it is a bug that gc.collect() doesn't do this.
#
# The following test is also based on the assumption that gc.collect()
# returns the number of objects it collects.  This is not true either.
# gc.collect() returns None.
#
# The following test is also based on the assumption that gc.collect()
# collects cycles of collectable objects.  This is not true either.
# gc.collect() collects cycles of *uncollectable* objects, but not
# cycles of collectable objects.  (There is no way to force it to
# collect cycles of collectable objects either.)
#
# The following test is also based on the assumption that gc.collect()
# collects objects which are reachable only through a chain of
# __del
