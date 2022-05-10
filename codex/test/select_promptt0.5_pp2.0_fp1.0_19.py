import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# return three lists corresponding to the first three arguments; each contains
# those entries from the argument list that are ready

# select() modifies the lists it is given, so you cannot use them for other
# purposes after calling select().

# If the timeout is omitted the select blocks until at least one file descriptor
# is ready.

# A negative or None timeout means to block indefinitely.

# A zero timeout means to never block.

# The select() function is a direct interface to the underlying operating
# system implementation.

# If the operating system uses a level-triggered interface, the returned lists
# will always be complete, that is, they will contain all the file descriptors
# that are ready.

# If the operating system uses a edge-triggered interface, the returned lists
# may be incomplete
