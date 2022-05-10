import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# Monitor sockets for I/O events.
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified (or None), block until an event occurs
# If a socket object is passed, the corresponding file descriptor is extracted.
# The return value is a triple of lists of objects that are ready: subsets of the first three arguments.
# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.
# If a file descriptor is encountered that is invalid, OSError will be raised.
# (On some platforms, ResourceWarning may also be raised.)
# The file descriptor lists are modified in place to reflect the descriptors that are still valid.

# select() 函数的原型定义为：
# select(rlist, wlist, xlist[, timeout])
#
