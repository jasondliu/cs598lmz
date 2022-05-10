import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select() returns three lists of objects that are ready: subsets of the first three arguments.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A negative or None timeout means to block indefinitely.

# select() may modify the lists it receives as arguments, and may also return modified copies of the lists.
# You should assume that this is the case and write your code accordingly.

# The objects that select() operates on are file descriptors, which are small integers given out by a call to the open() function.
# The file descriptor is an integer that uniquely identifies an open file in a computer’s operating system.
# A file descriptor is a non-negative integer.
# The value 0 is reserved for standard input, 1 is reserved for standard output, and 2 is reserved for standard error.

