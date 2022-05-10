import select
# Test select.select()
# https://docs.python.org/3/library/select.html

# select()
# select() takes three lists of objects: rlist, wlist, and xlist.
# The first list, rlist, is a list of objects that you want to wait until they are ready for reading.
# The second list, wlist, is a list of objects that you want to wait until they are ready for writing.
# The third list, xlist, is a list of objects that you want to wait for exceptions.

# select() returns three lists of objects that are ready: rlist, wlist, and xlist.
# If the time limit is exceeded before any object is ready, the three lists are returned as empty lists.

# select() will not work on Windows.

# select() can be used with pipes, sockets, and devices.

# select() is available on Unix and Windows.
# select() is not available on Mac.

# select() is used to monitor multiple file descriptors, waiting until one or more of the file descriptors become "ready" for some class of I/O operation (e.g., input
