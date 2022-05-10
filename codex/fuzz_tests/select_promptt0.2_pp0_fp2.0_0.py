import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)

# select.select() returns three lists of objects that are ready:
# rlist: those sockets ready for reading
# wlist: those sockets ready for writing
# xlist: those sockets with "exceptional conditions" (really uncommon)

# select.select() takes a fourth, optional, argument: a timeout.
# If the timeout argument is omitted, select.select() blocks until at least one file descriptor is ready.
# If the timeout argument is present and not None, it should be a floating point number specifying a timeout in seconds (or fractions thereof).
# The select.select() function returns a tuple of three lists of objects that are ready:
# rlist: those sockets ready for reading
# wlist: those sockets ready for writing
# xlist: those sockets with "exceptional conditions" (really uncommon)
# If the timeout is reached before
