import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# return value: three lists of objects that are ready

# timeout: if not specified, block until at least one file descriptor is ready
# if timeout is a number, it specifies a time-out as a floating point number in seconds
# if timeout is None, the call will never time out

# select.error: if a file descriptor is greater than FD_SETSIZE
# (1024 on most systems)

# select.select() is a blocking I/O multiplexing method
# it monitors multiple file descriptors, waiting until one or more of the file descriptors become “ready” for some class of I/O operation

# select.select() is useful for:
# 1. waiting for a response from a server
# 2. waiting for user input
# 3. waiting for a file to become available for reading
#
