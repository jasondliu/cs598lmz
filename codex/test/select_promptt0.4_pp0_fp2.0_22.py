import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Returns three lists of subset of the first three arguments: those descriptors that are ready, those that have an exceptional condition, those that timed out (only if a timeout is given)

# If the timeout is omitted the select blocks until at least one file descriptor is ready. A timeout of zero specifies a poll and never blocks.

# The select has a resolution of one second.

# If select() returns three empty lists, then timeout has expired and you can continue with other work.

# If select() returns three lists with at least one member, then work is pending on the descriptor(s) which have been returned.

# If select() returns immediately with three empty lists, then there is no work pending on any monitored file descriptor.

# If select() returns immediately with three lists containing at least one member, then there is work pending on the descriptor
