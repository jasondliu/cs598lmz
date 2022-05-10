import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready
# rlist: objects in rlist that are ready for reading
# wlist: objects in wlist that are ready for writing
# xlist: objects in xlist that have an “exceptional condition”

# select.select() is a blocking call.
# If you want to make it non-blocking, set a timeout value.
# If you set a timeout value of 0.0, it will return immediately.

# select.select() is available on Unix and Windows.
# On Unix, it supports file descriptors.
# On Windows, it supports sockets.

# select.select() is not available on standard input.
# Use select.poll() or select.epoll() instead
