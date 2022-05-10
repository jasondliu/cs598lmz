import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor is ready; if specified as a float, it specifies a timeout in seconds; if specified as None, it will block until a monitored file descriptor is ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, especially when you want to monitor multiple file descriptors at the same time.

# select.select() is available on Unix and Windows.

# select.poll()
# select.poll() is a more advanced version of select() available on Unix and Windows.

# select.poll() is a class that supports registering and unregistering file descriptors, and then polling them for I/O events.

# select.poll() is available on Unix and Windows.

