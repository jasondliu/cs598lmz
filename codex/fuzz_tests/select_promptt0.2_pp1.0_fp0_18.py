import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if a positive number, block for up to that many seconds and return three lists of file descriptors that are ready

# Return value: three lists of file descriptors that are ready

# select.select() is a useful way to multiplex input/output over a set of file descriptors.
# The first three arguments are sequences of file descriptors to be waited for: rlist, wlist, xlist.
# The first three arguments may be modified on return.

# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.

#
