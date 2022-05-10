import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, select() can block indefinitely

# select.select() returns three lists of objects that are ready:
# rlist: objects that are ready for reading
# wlist: objects that are ready for writing
# xlist: objects that have an “exceptional condition” (end of file, out-of-band data)

# select.select() can also be used with sockets:
# rlist, wlist, xlist = select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition”
# timeout: if not specified, select() can block indefinitely

# select.select() returns three lists of sockets that are ready:
#
