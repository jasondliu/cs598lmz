import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input and output,
# allowing your program to wait until any one of multiple I/O operations are ready before performing any of them.

# select.select() is also useful for implementing timeouts.
# If you pass a non-negative timeout value,
# it will block at most that many seconds and
# a three-tuple of lists of objects that are ready will be returned.

# If the timeout is omitted or None,
# the call will never time out.

# If the timeout is a positive value,
# it blocks at most timeout seconds and
# returns three lists of objects that are ready.

# If the timeout is zero,
# it will never block and
# always return three empty lists.
