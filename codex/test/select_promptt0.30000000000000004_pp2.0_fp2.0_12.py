import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, it specifies a timeout in seconds (float) and the function will return at most once after that many seconds have passed, even if no file descriptors are ready

# Returns three lists of file descriptors: those that are ready for reading, those that are ready for writing, and those that have an “exceptional condition” (an “exceptional condition” is defined by the underlying operating system).

# The first three arguments are sequences of file descriptors to be waited for: rlist, wlist, and xlist.
# All three arguments are optional; if the sequence is empty, it is treated as if it were a sequence with a single element, the current file descriptor of the process
