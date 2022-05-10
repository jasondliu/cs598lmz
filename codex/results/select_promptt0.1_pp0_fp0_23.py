import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor becomes ready; if supplied as a float with a nonzero value, block for that many seconds; if supplied as None, block until a monitored file descriptor becomes ready or the call is interrupted by a signal (see the PEP 475 for the rationale for this new value)

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a blocking call.
# select.select() is a low-level function.
# select.select() is not portable.
# select.select() is not thread-safe.
# select.select() is not interruptible.
# select.select() is not interruptible.
# select.select() is not interruptible.
# select.select() is not interruptible.
# select.select
