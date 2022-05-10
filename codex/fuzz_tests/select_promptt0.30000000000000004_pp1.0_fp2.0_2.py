import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.error: exception raised in case of an error

# select.select() can be interrupted by a signal (see the signal module)

# select.select() also works with file descriptors on systems that support the poll() system call.

# select.select() supports three file descriptor lists:
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition”

# select() returns three lists of objects that are ready:
# sublists of the first three arguments
# sublists are in the same order as the original lists
# objects on a sublist are the same objects as in the original list
# if the time limit is reached without a file descriptor becoming ready, three empty
