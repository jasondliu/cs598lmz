import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# If the timeout argument is omitted the select blocks until at least one file descriptor is ready.
# A timeout value of zero specifies a poll and never blocks.

# The return value is a triple of lists of objects that are ready:
# sublist for reading, sublist for writing, sublist for errors.

# The input lists are not modified.

# The objects in the return lists are file descriptors, not filenames.

# The file descriptors returned in the lists are the ones passed in the arguments.
# The file descriptors in the argument lists are checked in a non-blocking fashion.

# The returned lists contain no duplicates.

# The select function supports sockets, pipes and some other objects on some systems (e.g. Windows).
# It does not support arbitrary file-like objects.

#
