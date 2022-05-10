import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() can be used as a way to wait until a file is ready for reading or writing, or until a timeout has occurred.

# The select.select() function takes three lists of objects:

# The first is a list of objects to be checked for incoming data to be read (e.g. sockets or file descriptors).
# The second is a list of objects to be checked for readiness for writing (e.g. sockets or file descriptors).
# The third is a list of objects to be checked for “exceptional conditions” (e.g. sockets or file descriptors).
# The return value is a tuple of three lists of objects that are ready:

# The first list contains objects that are ready for reading.
# The second list contains objects
