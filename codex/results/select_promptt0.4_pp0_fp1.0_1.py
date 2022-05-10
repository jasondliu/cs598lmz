import select
# Test select.select()
# select.select() is used to monitor multiple file descriptors, waiting until one or more of the file descriptors become "ready" for some class of I/O operation (e.g., input possible).
#
# The first three arguments to select() are three lists of file descriptors to be monitored.
# The first list contains the file descriptors to be checked for being "ready for reading", the second contains the file descriptors to be checked for being "ready for writing", and the third contains file descriptors to be checked for errors.
#
# The fourth argument to select() is the timeout, which is the maximum time to wait before returning.
# If the timeout is omitted, select() can block indefinitely.
#
# The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready.
#
# The optional argument to select() is a bit mask of file descriptors to be checked.
# The default value of this argument is 0, so by default all file descriptors are checked.
# The bit mask is formed by ORing together zero or more of the constants defined in the module.
