import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a file descriptor is ready

# Return value: three lists of objects that are ready

# select.error: exception raised in case of an error

# select.select() is a useful way to multiplex input and output,
# allowing your program to monitor multiple file descriptors at once
# and determine which ones are ready for reading, writing, or an exception condition.

# select.select() is available on all platforms that support the select() system call.
# On Windows, it supports sockets only.

# select.poll() is available on most Unix platforms, and works with any file descriptor.
# It also supports a more efficient way to monitor sockets,
# but requires more setup and is not available on Windows.

# select.epoll() is available on Linux 2.6 and later
