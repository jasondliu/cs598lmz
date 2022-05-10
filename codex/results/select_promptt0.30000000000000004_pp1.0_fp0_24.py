import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select.select() returns three lists of objects that are ready:
# sublists of the first three arguments.
# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the time-out argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.

# When select() returns, the objects in the lists are updated to reflect the actual status of the file descriptors.
# On some systems, the function may also return an additional fourth object,
# which is the object that caused the return.

# The select() function is a way to poll the operating system to see if a file descriptor is ready for reading or writing.
# The select() function is available on Unix and on Windows.
# The select() function is not
