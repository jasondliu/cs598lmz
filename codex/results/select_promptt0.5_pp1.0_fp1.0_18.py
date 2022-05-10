import select
# Test select.select()
#
# select.select() takes three lists of objects to watch for I/O readiness:
#
#  rlist: wait until ready for reading
#  wlist: wait until ready for writing
#  xlist: wait for an "exceptional condition" (see the manual page)
#
# It can also take a fourth, optional parameter, "timeout" -- the maximum
# time to wait, in seconds.  If "timeout" is omitted, select.select() will
# block until at least one file descriptor is ready.
#
# The return value is actually a tuple of three lists corresponding to
# the first three arguments; each contains the subset of the corresponding
# file descriptors that are ready.
#
# The following example waits for stdin to be ready, but only for five
# seconds.  If stdin is not ready within five seconds, it times out and
# proceeds.

import sys
import select

print 'I/O multiplexing with select()'
print 'Waiting for stdin to be ready...'
rlist, wlist, xlist = select.select([sys.stdin], [
