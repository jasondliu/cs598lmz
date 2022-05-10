import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# 	rlist: wait until ready for reading
# 	wlist: wait until ready for writing
# 	xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# 	timeout: (optional) if None, then block until a file descriptor is ready. If 0, then return immediately. If x, block for x seconds.

# Returns three lists of file descriptors: subsets of the first three arguments
# 	rlist: those file descriptors that are ready for reading
# 	wlist: those file descriptors that are ready for writing
# 	xlist: those file descriptors that have an "exceptional condition" (see the manual page for what your system considers such a condition)

# File descriptor: a number that uniquely identifies an open file in a computer's operating system.

# select.select() returns the file descriptors that are ready for reading, writing, or an exceptional condition.

# select.select() is a blocking function.

# select.select()
