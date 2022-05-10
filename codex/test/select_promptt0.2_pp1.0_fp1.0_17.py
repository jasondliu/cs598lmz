import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])

# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# timeout: if not specified or None, select() can block indefinitely
# if specified as a float, it specifies a timeout in seconds
# if specified as an integer, it specifies a timeout in milliseconds

# Return value: three lists of objects that are ready

# select.select() is a blocking call.
# select.select() is a low-level function that does not have a file descriptor limit.
# select.select() is available on all platforms (Windows, Linux, MacOS X, etc.)

# select.poll() is a non-blocking call.
# select.poll() is a high-level function that has a file descriptor limit.
# select.poll() is not available on all platforms (Windows, Linux, MacOS X, etc.)

# select.epoll() is a non-blocking call.
#
