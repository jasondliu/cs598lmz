import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# For example, select.select([sys.stdin], [], [], 0.0)[0] will return a list containing sys.stdin if a line is ready to be read.
# select.select([sys.stdin], [], [], 0.0)[0] will return an empty list if no line is ready to be read.

# select.select([sys.stdin], [], [], 0.0)[0] will return an empty list if no line is ready to be read.
# select.select([sys.stdin], [], [], 0.0)[0] will return an empty list if no line is ready to be read.
# select.select([sys.stdin], [], [], 0.0)[0] will return an
