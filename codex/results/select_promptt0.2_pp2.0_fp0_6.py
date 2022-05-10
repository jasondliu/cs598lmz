import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, it specifies a timeout in seconds (float allowed) after which select() returns even if no file descriptors are ready

# Return value: three lists of file descriptors: rlist, wlist, xlist

# select() can be told to monitor only a subset of the file descriptors by passing in optional lists of file descriptors to monitor for reading, writing, and exceptional conditions.
# If the lists are empty, select() can be told to block indefinitely, or it can return immediately, depending on the value of the optional timeout parameter.
# If the timeout is omitted, it defaults to -1, which means to block indefinitely.
# If the timeout is zero, select() returns immediately, even
