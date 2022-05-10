import select
# Test select.select

# select.select([r],[w],[e])
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: in seconds
# if timeout is omitted, select() can block indefinitely
# if timeout is zero, select() will never block and will return three lists of zero length if there is nothing to do

# return value: three lists of objects that are ready: subsets of the first three arguments
# If the time-out is reached without a file descriptor becoming ready, three empty lists are returned
# select.error: if an error occurs
# select.error: if the file descriptor is negative
# select.error: if the file descriptor is greater than FD_SETSIZE

# Python 2.x:
# rlist, wlist, xlist = select.select(rlist, wlist, xlist[, timeout])
# Python 3.x:
# rlist, wlist,
