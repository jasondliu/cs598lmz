import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist are lists of file descriptors to be waited for
# timeout is an optional integer timeout in seconds
# select() returns three lists of file descriptors: those that are ready for reading, writing and exceptional conditions
# If the timeout is omitted, it blocks until at least one file descriptor is ready
# If the timeout is zero, it never blocks and returns three empty lists
# If the timeout is negative, it blocks indefinitely
# If a file descriptor appears in all three lists, it will be returned only once
# If a file descriptor appears in both rlist and xlist, it will be returned only in xlist
# If a file descriptor appears in both rlist and wlist, it will be returned only in wlist
# If a file descriptor appears in both xlist and wlist, it will be returned only in wlist

# Test select.poll()
# select.poll() returns a polling object, which supports registering and unregistering file descriptors, and then polling them for I/O events
# poll() is a more efficient way to wait for
