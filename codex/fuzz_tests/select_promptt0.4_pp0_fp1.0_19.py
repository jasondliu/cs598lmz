import select
# Test select.select()
#
#

# select.select()
# select.poll()
# select.epoll()
# select.kqueue()

# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: a time-out as a floating point number in seconds (or None for no time-out)
#
# Return value: three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready.
#
# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g., read()) without blocking.
#
# select() may modify the lists it receives as arguments, and may also return modified copies of the lists.

# select.poll()
# select.poll()
#
# class select.poll()
#
# Create a polling object.
#
# A polling object supports registering and un
