import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# The return value is a triple of lists of objects that are ready:
# (subset of rlist, subset of wlist, subset of xlist)

# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.

# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# Note: select() may modify the lists it receives as arguments, so you should pass them in as copies.

# Note: select() should not be used if you can use poll() or epoll().

# Note: select() supports file descriptors greater than FD_SETSIZE, but some non-Unix systems have
