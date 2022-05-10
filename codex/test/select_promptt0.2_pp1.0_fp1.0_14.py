import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select() can be told to return when an object is ready for reading, when an object is ready for writing, or when an object has an “exceptional condition” (exception) pending.

# select() can be used as a sleep() function.

# select() can be used to monitor multiple sockets at the same time.

# select() can be used to monitor a single socket.

# select() can be used to monitor a file descriptor.

# select() can be used to monitor a file object.

# select() can be used to monitor a file-like object.

# select() can be used to monitor a file descriptor or file object.

# select() can be used to monitor a file descriptor or file-like object.

#
