import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor becomes ready; if supplied as a float, block that many seconds; if supplied as None, block indefinitely

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor becomes ready; if supplied as a float, block that many seconds; if supplied as None, block indefinitely

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select(
