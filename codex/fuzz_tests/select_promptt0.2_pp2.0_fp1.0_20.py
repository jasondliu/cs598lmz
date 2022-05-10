import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready
#
# Return value:
#
# Three lists are returned, one for each of the specified lists of file descriptors.
# Each list contains the subset of the corresponding file descriptors that are ready for the specified operation.
#
# If the timeout is reached before any file descriptors become ready, three empty lists are returned.
#
# If the timeout is zero and at least one file descriptor is ready, the lists returned contain only those file descriptors that are ready.
#
# If the timeout is zero and no file descriptors are ready, three empty lists are returned.

# The select() function is a useful tool for multiplexing input and output.
# It allows you to wait for input on multiple file descriptors at the same time.
#
