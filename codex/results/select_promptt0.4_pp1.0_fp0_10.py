import select
# Test select.select()
#
# select.select() takes three lists of file descriptors and waits until
# some of them are ready for I/O.  The first list is the one to wait for
# reading, the second for writing, and the third for errors.  When one or
# more of these conditions is met, the list of ready file descriptors is
# returned.  The lists are modified in place to remove the descriptors
# that are ready.  The return value is a tuple of three lists of
# descriptors, one for each condition that was met.
#
# The optional timeout argument specifies a time-out as a floating point
# number in seconds.  When the timeout argument is omitted the function
# blocks until at least one descriptor meets the specified condition.  A
# time-out value of zero specifies a poll and never blocks.
#
# The following example illustrates the use of select() to multiplex
# reading from standard input and a TCP/IP socket.  It assumes that the
# socket is in blocking mode.
#
# The example is written for Python 2.6.

import socket
import sys

# Create a TCP/
