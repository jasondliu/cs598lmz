import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor is ready; if specified as a float, it specifies a timeout in seconds (as a fraction of a second); if specified as an integer, it specifies a timeout in milliseconds; if specified as None, it will never time out

# select() can monitor sockets, open files, or pipes (anything with a fileno() method that returns a valid file descriptor).
# If you want to monitor more than one of these objects, use multiple select() calls, one for each object, in your main loop.
# Typical return value:
#    three lists of objects: subsets of the first three arguments
#    that are ready: r, w, x = select.select(rlist, wlist, xlist[, timeout])

# select() is a useful tool for creating network servers.
# If you are creating a
