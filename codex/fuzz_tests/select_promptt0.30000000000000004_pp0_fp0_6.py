import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# The return value is a triple of lists of objects that are ready:
# (subset of rlist, subset of wlist, subset of xlist)

# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.

# The select() function monitors all socket objects and pipes (anything with a fileno() method that returns a valid file descriptor)
# until they become readable, writable or have an exception condition pending, respectively.
# The first three arguments are sequences of socket objects, and the last one is a timeout value in seconds.
# The return value is a tuple of three lists corresponding to the first three arguments;
# each contains the subset of the
