import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Returns three lists of objects that are ready: subsets of the first three arguments.
# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.

# The return value is a triple of lists of objects that are ready:
#   subsets of the first three arguments.
# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# Example:
#   >>> import select
#   >>> iwtd, owtd, ewtd = select.select([sys.stdin], [], [], 10.0)
#   >>> if iwtd:
#   ...     print('You said:
