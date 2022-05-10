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
# If you want to wait forever, set timeout to None or leave it unspecified.

# select.select() is a low-level function.
# For a higher-level abstraction, see the asyncio module.

# select.select() is not available on all platforms.
# On Windows, it only works for sockets; on Unix, it also works for other
