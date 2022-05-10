import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# The select() function monitors all sockets and pipes given in the lists.
# If a socket or pipe is ready, it is added to the appropriate list.
# If a socket or pipe has an error, it is added to the list of exceptional conditions.
# If a socket or pipe has been closed, it is removed from all lists.
# If a socket or pipe is not monitored, it is ignored.

# The timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.

# When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the operation in seconds (
