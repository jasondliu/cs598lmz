import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# Return three lists of objects that are ready for I/O.
# rlist, wlist, xlist are lists of objects to be tested for readability, writability, and exceptional conditions.
# timeout is a floating point number specifying the timeout in seconds.
# If timeout is omitted, select() blocks until at least one of the specified conditions is true.

# select() returns three lists of objects that are ready for I/O.
# The first list contains objects that are ready for reading,
# the second list contains objects that are ready for writing,
# and the third list contains objects that have an exceptional condition pending.

# select() is a useful tool for multiplexing I/O.
# It is the basis for the select module and for the epoll module.

# The select module is a wrapper around the select system call.
# It supports the same arguments as the system call,
# but the object lists are replaced by Python lists.

# The epoll module is a wrapper around the epoll system call.
# It supports the same arguments as the
