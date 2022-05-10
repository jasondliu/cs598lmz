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
# If a timeout is given and no file descriptor is ready, the function will block for at most timeout seconds.
# If the timeout is reached without a file descriptor becoming ready, three empty lists are returned.
# If the timeout is zero, then select() won’t block at all and will return three empty lists immediately if no file descriptors are ready.

# select.select() is available on Unix and Windows.
# On Unix, it
