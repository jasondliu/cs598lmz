import select
# Test select.select()
#
# select() takes three lists of file descriptors and waits until one or more
# of the descriptors are ready for some kind of I/O. The first list
# contains the descriptors we're waiting to become readable, the second
# contains the descriptors we're waiting to become writeable, and the
# third contains the descriptors we're waiting for an "exceptional
# condition" (we're not going to cover these exceptions here).
#
# The return value is actually a triple of lists corresponding to the
# first three arguments; each contains the subset of the corresponding
# file descriptors that are ready for the given operation.
#
# The optional timeout argument specifies a time-out as a floating point
# number in seconds. When the timeout argument is omitted the function
# blocks until at least one descriptor is ready. A time-out value of zero
# specifies a poll and never blocks.
#
# The select() function is a direct interface to the underlying operating
# system implementation. It relies on a fixed sized list of file descriptors,
# which vary by platform:
#
#   Platform	Maximum file descriptors
#   --------------------------------
