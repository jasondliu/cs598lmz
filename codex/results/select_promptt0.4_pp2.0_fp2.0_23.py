import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: If None, then select() can block indefinitely. If 0, then it will never block. Otherwise, it will block for timeout seconds.
# Return value: three lists of objects that are ready: subsets of the first three arguments.

# select.select() is a blocking call.

# select.select() will return three lists of objects that are ready: subsets of the first three arguments.
# If the time limit is reached, three empty lists are returned.

# select() only works on sockets.

# select() is available on all platforms (Linux, Windows, Unix, BSD).
# select() is not available on Mac OS X.
# select() is not available on Android.

# select() is available on Python 2 and Python 3.

# select() is not available on Jython.

# select
