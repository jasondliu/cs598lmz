import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until at least one file descriptor is ready
# returns three lists of objects that are ready: subsets of the first three arguments
# if the timeout is reached before anything interesting happens, return three empty lists

# select.error
# exception raised in the event of exceptional errors
# this is a subclass of OSError

# select.select_error
# exception raised in the event of invalid arguments passed to the select() function
# this is a subclass of select.error

# select.poll()
# select.poll() is an efficient implementation of a polling object
# a polling object supports registering and unregistering file descriptors, and then polling them for I/O events
# select.poll() is available on Unix and Windows
# select.poll() returns a list of tuples
# each tuple contains
