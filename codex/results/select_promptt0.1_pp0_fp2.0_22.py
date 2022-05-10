import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.error: exception raised in case of an error

# select.select() can be interrupted by a signal (see the signal module)

# select.select() supports the following object types:
# - file descriptors
# - sockets
# - pipes (on Unix)
# - anything with a fileno() method that returns a valid file descriptor

# select.select() does not support the following object types:
# - sockets for which a timeout is set
# - sockets which are not in blocking mode
# - sockets which have had timeouts set using the settimeout() method
# - sockets which have had a timeout set using setdefaulttimeout()

# select.select() can be used to monitor multiple file descriptors, waiting until one or more of the file descriptors
