import select
# Test select.select()
# https://docs.python.org/3/library/select.html

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not None, an integer number specifying a timeout in seconds

# Return value:
# Three lists are returned, one for each of the three sets of descriptors. The first list contains those descriptors that are ready for reading, the second contains those that are ready for writing, and the third those that have an exceptional condition pending.
# If the timeout is reached without any of the monitored events occurring, three empty lists are returned.

# Notes:
# The returned lists contain only the objects that are ready; if a file descriptor is in the list but not ready, it is silently removed from the returned list.
# The returned lists are unordered.
# When the timeout argument is omitted the function blocks until at least one descriptor is ready.
# A negative or None timeout
