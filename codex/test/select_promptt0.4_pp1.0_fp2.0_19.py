import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (not used on Windows)

# Return value: three lists of objects that are ready

# select.select() takes three lists of objects, waits until one or more of the objects is ready, and returns three lists containing subsets of the original lists.

# The first list contains objects that are ready for reading, the second contains objects that are ready for writing, and the third contains objects that have raised exceptions.

# The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument is omitted the function blocks until at least one of the objects is ready. A time-out value of zero specifies a poll and never blocks.

# A time-out value of None specifies an unbounded wait. The function will block until at least one of the objects is ready.

# If the time-out is reached before an object is ready, three empty lists are returned.

# The select()
