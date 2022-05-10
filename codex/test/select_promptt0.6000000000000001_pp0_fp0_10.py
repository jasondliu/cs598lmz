import select
# Test select.select()
# This is not a program, but a test suite.
#
# The select.select() API takes three lists of file descriptors:
# (rlist, wlist, xlist[, timeout])
# and waits until they are ready for reading, writing or have an
# exceptional condition (respectively).
#
# The file descriptors in each list can be sockets, pipes or
# anything else with a fileno() method that returns a valid file
# descriptor.
#
# The select() call will return three lists of file descriptors:
# (rlist, wlist, xlist)
# which correspond to the entries in the three lists passed to
# select() that are ready for the specified operation.
#
# This test suite uses pipes and sockets to test the functionality.
#
# See the Library Reference Manual section on the select module.

import unittest
from test import support
import select as _select

HAVE_GETEVENTS = hasattr(_select, "epoll")
HAVE_DEV_POLL = hasattr(_select, "devpoll")

# A more realistic timeout than the original test
