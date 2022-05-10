import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# Example:
# rlist, wlist, xlist = select.select([sys.stdin], [], [], 0.0)
# if rlist:
#     s = sys.stdin.readline()
#     ...
# else:
#     ...

# select.poll()
# select.poll() is a cross-platform alternative to select() that works on non-Unix platforms.
# It supports the same operations as select(), but it returns a poll object, which has three methods:
# register(fd[, eventmask])
# unregister(fd)
# poll([timeout])

# The eventmask argument to register
