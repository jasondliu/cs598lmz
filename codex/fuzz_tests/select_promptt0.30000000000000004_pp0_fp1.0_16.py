import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# select.select() returns three lists of objects that are ready: subsets of the first three arguments.
# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.
# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g., read(2) without blocking, or a sufficiently small write(2)).
# The following example shows how to use select() to monitor three file descriptors (0, 1 and 2, the standard input, output and error file descriptors of the current process) and wait until one of them is ready for reading:

import sys, select

print('Please enter something:')
rlist, _, _ = select.select([sys.stdin], [], [], 10
