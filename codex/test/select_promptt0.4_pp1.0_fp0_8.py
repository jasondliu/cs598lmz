import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
#
# Return value:
#
# Three lists are returned, one for each of the three sets of descriptors.
# The first list contains those descriptors that are ready for reading,
# the second contains those that are ready for writing, and the third
# contains those that have seen “exceptional conditions”.
#
# If only one kind of condition is required, pass [] for the other lists.
#
# A descriptor is ready if it is possible to perform the corresponding
# I/O operation (e.g. read()) without blocking.
#
# If the timeout is omitted, it defaults to zero, i.e. the call will never block.
# If the timeout is zero and there are no events to report, select() will return three empty lists.
#
# If the timeout is a positive number
