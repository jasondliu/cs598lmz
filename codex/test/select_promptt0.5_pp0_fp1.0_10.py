import select
# Test select.select()

# select.select() is used to monitor multiple file descriptors for events
# only works on sockets, pipes, and devices
# does not work on files

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (oob data or signal)
# timeout: time to wait in seconds
# returns 3 lists of objects that are ready

# Example: wait for keyboard input
# rlist, wlist, xlist = select.select([sys.stdin], [], [], 1)
# if rlist:
#     s = sys.stdin.readline()
#     print s

# Example: wait for a socket to be ready for writing
# rlist, wlist, xlist = select.select([], [sock], [], 1)
# if wlist:
#     sock.send("spam")

# Example: wait for a socket to be ready for reading or for an exception
# rlist, wlist, xlist
