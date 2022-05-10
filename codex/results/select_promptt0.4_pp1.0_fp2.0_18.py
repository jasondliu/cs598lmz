import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified or None, block until at least one file descriptor is ready; otherwise, block at most timeout seconds and raise the exception if no file descriptor is ready during that time

# return three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready

# select.select() is a great way to wait for multiple events at the same time
# It can be used to wait for a ready socket and also for stdin input at the same time

# select.select() is available on Unix and Windows
# On Unix, it’s available as the select module
# On Windows, it’s available as the msvcrt module
# On Unix, select.select() can be used to monitor multiple file descriptors
# On Windows, it can be used to monitor only sockets

#
