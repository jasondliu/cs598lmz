import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select() returns three lists of objects that are ready: subsets of the first three arguments.
# When the timeout argument is omitted it blocks until at least one file descriptor is ready.
# A zero timeout causes select() to return immediately, even if no file descriptors are ready.

# select() may modify the lists it receives as arguments, and may also return empty lists.
# You should never rely on the lists being the same after select() returns.

# select() can be interrupted by a signal (see the signal module).
# In that case it returns three empty lists.

# select() should not be used if you can use poll() or epoll().
# They are faster and more scalable.

# select() supports file descriptors greater than FD_SETSIZE, but some platforms have an artificial limit
# on the value that can
