import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])

# Return three lists of objects that are ready for reading, writing and
# in an exceptional condition respectively.

# If only one kind of I/O is requested, pass [] as the list not
# requested.

# The optional timeout argument specifies a time-out as a floating point
# number in seconds. When the timeout argument is omitted the function
# blocks until at least one file descriptor is ready. A time-out value
# of zero specifies a poll and never blocks.

# If the timeout argument is present and not None, it should be a
# floating point number specifying a timeout for the operation in
# seconds (or fractions thereof).

# This actually returns a triple of lists of objects that are ready:
# (rlist, wlist, xlist)
#
# The first of these, rlist, is a list of objects that are ready for
# reading.  The second, wlist, is a list of objects that are ready for
# writing.  The third, xlist, is a list of objects that have had
# exceptions raised.
