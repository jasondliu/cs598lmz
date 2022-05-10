import select
# Test select.select function

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a file descriptor is ready

# Return value: three lists of objects that are ready
# rlist: objects in rlist that are ready for reading
# wlist: objects in wlist that are ready for writing
# xlist: objects in xlist that have an “exceptional condition”

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a file descriptor is ready

# Return value: three lists of objects that are ready
# rlist: objects in rlist that are ready for
