import select
# Test select.select()

# 1. select.select()
# 2. select.poll()
# 3. select.epoll()
# 4. select.kqueue()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select.select() returns three lists of objects.
# The first contains objects that are ready for reading,
# the second contains objects that are ready for writing,
# and the third contains objects that have raised an exception.

# select.select() is a blocking call.
# If the timeout is omitted, it will block until at least one file descriptor is ready.
# If the timeout is zero, it will never block and return three empty lists.
# If the timeout is a positive number, it will block for at most that many seconds and return three lists of file descriptors that are ready.
# If the timeout is negative, it will block forever.

# select.select()
