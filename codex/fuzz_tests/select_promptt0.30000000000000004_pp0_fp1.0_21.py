import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select() returns three lists of objects that are ready: subsets of the first three arguments.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A zero timeout causes the function to return immediately, even if no file descriptors are ready.
# If the timeout argument is present and not None, and the timeout period value has elapsed,
# three empty lists are returned.

# The file objects in the lists returned by select() are not guaranteed to be in any particular order.

# select() may modify the lists it receives as arguments, and may also return modified copies of those arguments.
# The objects in the lists may be modified by other threads after select() returns but before they are accessed by the current thread.
# The select() function should be reentrant and may be called by other threads while a previous select
