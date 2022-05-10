import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, select() can block indefinitely

# select() returns three lists of objects that are ready: subsets of the first three arguments.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g. read()) without blocking.
# (For the select() function, only the reading operations are considered; in a real-world program, you will want to check for both reading and writing.)

# The select() function is a direct interface to the underlying operating system implementation.
# It’s less portable than the alternatives, but it’s efficient.
# It’s also the only way to perform truly asynchronous I/O in Python.

# The select() function is available on
