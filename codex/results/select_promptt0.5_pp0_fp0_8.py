import select
# Test select.select()
#
#  select.select(rlist, wlist, xlist[, timeout])
#
#  rlist: wait until ready for reading
#  wlist: wait until ready for writing
#  xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
#
#  returns three lists of objects that are ready: subsets of the first three arguments
#
#  timeout: if omitted or None, block until at least one descriptor is ready;
#           if 0, return three empty lists;
#           if >0, block for up to that many seconds and return three lists of objects that are ready
#
#  select() is useful if you want to monitor multiple sockets at once and don’t want to use threads.
#  select() can be used to monitor multiple sockets for incoming data,
#  to see when some socket has enough outgoing buffer space to send more data,
#  or to monitor a socket for availability to connect.
#
#  select() is available on Unix and on Windows.
#  On Unix, it supports file descriptors.

