import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block up to that many seconds

# Return value: three lists of file descriptors as above
# If the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# On Windows, only sockets are supported; on Unix, all file descriptors can be used.
# On Windows, if the timeout is zero, the return value may be three empty lists or two empty lists and a list with a socket object in it;
# the former behavior is a bug and may be fixed in a future version.

# !!! On Windows, select() only works on sockets, and some functions, such as ntohl() and gethostbyname_ex(), do not work on sockets.
# !!! On
