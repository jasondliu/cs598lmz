import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sources.
# For example, you can use it to wait for input from both a network connection and standard input at the same time.

# select.select() is also useful for implementing timeout functionality in your programs.
# If you pass a non-zero timeout value, select() will block for at most that many seconds.
# If the timeout expires before anything interesting happens, select() will return three empty lists.

# select.select() is available on Unix and Windows systems.

# select.select() is a useful way to multiplex input from multiple sources.
# For example, you can use it to
