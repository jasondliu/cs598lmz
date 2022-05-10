import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
#
# The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready.
#
# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g., read(2)) without blocking.
#
# (Thus, the results of the call to select() are a snapshot of the file descriptor sets; if a file descriptor is ready at the time it is tested, it may be subsequently blocked.
#
# The file descriptor sets are modified in place to reflect the results of the call to select().
#
# The timeout argument specifies a time-out as an integer number of seconds;
#
# if it is omitted or None, the call will never time out.
#
# The return value is a tuple of three lists of file
