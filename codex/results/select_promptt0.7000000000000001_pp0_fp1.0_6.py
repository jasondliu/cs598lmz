import select
# Test select.select
#
# select.select(rlist, wlist, xlist[, timeout])
#
#
# rlist, wlist, xlist -- lists of selectable objects
#
# The first three arguments are sequences of objects to be waited for:
# rlist -- wait until ready for reading
# wlist -- wait until ready for writing
# xlist -- wait for an ``exceptional condition'' (see the manual page)
#
# If only one kind of condition is required, pass [] for the other lists.
#
# A file object is ready for reading if a call to its read() method will not
# block. A file object is ready for writing if a call to its write() method
# will not block.
#
# A file object is ready for an exceptional condition if an exceptional
# condition has occurred on the underlying file descriptor.
#
# Note that if the file descriptor is a regular file, always ready for an
# exceptional condition, so if you are interested in such a condition, you
# have to specify at least one exceptional condition.
#
# Changed in version 2.6: Some platforms (specifically FreeBSD 6.0
