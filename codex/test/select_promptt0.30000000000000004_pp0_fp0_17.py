import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return immediately even if no file descriptors are ready; if given, it should be a float giving a timeout in seconds (or fractions thereof)

# The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# select() may modify any of the lists it is passed.

# select() supports three file descriptor sets, for reading, writing, and errors. The first three arguments to select() are the three file descriptor sets, represented as Python lists. The first three lists passed to select() are not modified by select().

# The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument
