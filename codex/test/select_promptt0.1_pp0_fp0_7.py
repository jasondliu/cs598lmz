import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.error: exception raised in case of an error

# select.select() supports three file objects:
# regular files, sockets, and pipes (on Unix)

# select.select() does not support file objects such as terminals, ttys, etc.

# select.select() does not support file objects opened in append mode

# select.select() does not support file objects opened in non-blocking mode

# select.select() does not support file objects opened in text mode

# select.select() does not support file objects opened in binary mode

# select.select() does not support file objects opened in universal newline mode

# select.select() does not support file objects opened in buffered mode

# select.select() does not support file
