import select
# Test select.select()
#select.select() sends IO events to one or more file descriptors, allowing for platform-independent multiplexing.
# select(rlist, wlist, xlist[, timeout])
 # Three lists of file descriptors are checked:
 #
 # rlist: wait until ready for reading,
 # the first is the “server descriptor”, this parameter is a “list” in python ([]), and 0 is used to receive all events.
 # wlist: wait until ready for writing.
 # xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition).
 # timeout: If not given (or if None), block until at least one descriptor is ready.
 # If a float is given, it blocks at most timeout seconds and returns three lists after timeout seconds if nothing has happened.

 # Return value: three lists are returned, one for each channel.
 # They contain the communication channels that have been selected.

import select, socket
s = socket.socket()
s.connect(('www.baidu.com', 80))
s.setblocking(False)

