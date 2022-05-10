import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input/output over a set of file descriptors.
# It can be used to implement a simple web server, for example.

# select.select() can also be used to monitor multiple sockets for activity and only block the current thread
# when no sockets are ready for processing.

# select.select() is available on all platforms (Windows, Linux, Mac, etc.).
# On Unix, it supports file descriptors greater than 1024 on some platforms,
# and it can be interrupted by a signal (this is not supported on Windows).
# On Windows, it only works on sockets, and it does not support timeouts
