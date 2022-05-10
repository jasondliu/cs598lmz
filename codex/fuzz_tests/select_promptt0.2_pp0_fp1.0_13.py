import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, it specifies a timeout in seconds (float) and the function will return three lists after that time if no file descriptors became ready

# Return value: three lists of objects that are ready: subsets of the first three arguments
# If the time-out is reached without a file descriptor becoming ready, three empty lists are returned.
# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g., read(2) without blocking, or a sufficiently small write(2)).
# The following table shows the correspondence between the first three arguments, the return value, and the appropriate POSIX select(2) call:
# rlist, wlist, xlist	
