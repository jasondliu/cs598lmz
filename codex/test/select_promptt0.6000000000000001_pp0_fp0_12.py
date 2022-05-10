import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])

# rlist, wlist, xlist are lists of selectable objects.
# The return value is a tuple of three lists containing the objects that are ready:
# (rlist, wlist, xlist)
# A selectable object is one on which the methods fileno() and recv() are defined and on which fileno() returns a valid file descriptor.
# If timeout is not specified or is None, the call blocks until at least one of the lists is ready.
# If timeout is 0, the call will never block and will return three empty lists.
# If timeout is a positive integer, the call will block for at most timeout seconds and will return three lists of objects that are ready.

# In the case of a timeout it returns three empty lists.

# select() can be used as follows to watch for incoming data on several sockets at the same time:
# rlist, wlist, xlist = select.select(rlist, wlist, xlist[, timeout])
# The call blocks until at least one of the following conditions is true:
#
