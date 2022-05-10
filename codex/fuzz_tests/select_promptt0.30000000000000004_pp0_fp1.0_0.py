import select
# Test select.select()

# select.select() is used to monitor multiple file descriptors, waiting until one or more of the file descriptors become "ready" for some class of I/O operation (e.g. input possible).

# The first three arguments are sequences of 'waitable objects': either integers representing file descriptors or objects with a parameterless method named fileno() returning such an integer:

# select.select(rlist, wlist, xlist[, timeout])
# Wait until one or more file descriptors are ready for some kind of I/O. The first three arguments are sequences of file descriptors to be waited for: rlist -- wait until ready for reading wlist -- wait until ready for writing xlist -- wait for an ``exceptional condition'' If only one kind of condition is required, pass [] for the other lists. A file descriptor is ready if it is possible to perform the corresponding I/O operation (e.g. read(2) without blocking, or a sufficiently small write(2)). The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument is omitted the function blocks until at least one file descriptor is ready. A time
