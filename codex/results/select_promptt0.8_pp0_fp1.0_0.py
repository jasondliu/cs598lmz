import select
# Test select.select
# http://docs.python.org/library/select.html#select.select

# select.select(rlist, wlist, xlist[, timeout])

if __name__ == '__main__':
    # The select function is a powerful tool that can be used to watch
    # multiple file descriptors at once and see if they become available
    # for I/O.  File descriptors can be sockets, file objects, pipes, or
    # anything else that behaves like a file descriptor.

    # The first three arguments to the select function are sequences of
    # file descriptors to be watched.  The first is a sequence of file
    # descriptors to be checked for availability for reading, the second
    # is a sequence of file descriptors to be checked for availability for
    # writing, and the third is a sequence of file descriptors to be checked
    # for errors.  The fourth argument is the timeout in seconds, and may be
    # either a floating point number or None.  Timeout specifies how long
    # the select function will wait for one of the specified conditions to
    # occur.  If timeout
