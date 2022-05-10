import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# select() returns three lists of file descriptors: subsets of the first three arguments.
# The first list contains those descriptors that are ready for reading,
# the second contains those ready for writing, and the third those that have an exceptional condition pending.
# The timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.

# select() may not report a socket file descriptor as ready for writing,
# even if it is. This is because some network stacks buffer data internally
# and only transmit it when the buffer is full, so a successful call to send()
# does not mean that
