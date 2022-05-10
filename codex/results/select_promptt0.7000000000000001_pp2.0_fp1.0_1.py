import select
# Test select.select()

# Use select.select() to monitor multiple file descriptors.
#
# Returns three lists of file descriptors:
#   read_ready: file descriptors ready for reading
#   write_ready: file descriptors ready for writing
#   in_error: file descriptors with exceptions (rare)
#
# The first three arguments are sequences of file descriptors to be monitored:
#   rlist: wait until ready for reading
#   wlist: wait until ready for writing
#   xlist: wait for an ``exceptional condition'' (we won't cover this)
#
# The optional fourth argument specifies a timeout in seconds; it may be
# specified as a float, to specify fractions of seconds.  If it is absent
# or None, the call will never time out.
#
# The return value is a tuple of three lists of file descriptors: those
# that are readable, writable, and have an exceptional condition (rare).

# This example shows how to use select() to monitor two sockets
# (including a server socket) at the same time.

# Set up some global variables

# This
