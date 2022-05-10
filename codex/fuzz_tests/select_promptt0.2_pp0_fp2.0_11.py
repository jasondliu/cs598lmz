import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, it specifies a timeout in seconds (float allowed) after which select() returns even if no file descriptors are ready

# Return value: three lists of file descriptors: rlist, wlist, xlist

# select() monitors only file descriptors, not file objects.

# select() can monitor sockets, pipes and devices.

# select() can monitor multiple file descriptors at once.

# select() can monitor file descriptors in different processes.

# select() can monitor file descriptors in different threads.

# select() cannot monitor file objects.

# select() cannot monitor files.

# select() cannot monitor directories.

# select() cannot monitor
