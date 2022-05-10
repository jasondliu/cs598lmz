import select
# Test select.select()
#
# Code based on example in Python docs ( https://docs.python.org/2/library/select.html )
#
# Notes:
#    select.select can be used to monitor multiple IO sources, and to return
#    when one or more are ready for IO (or a timeout); e.g. it can be used to
#    monitor IO from a remote device and from a user's terminal, and perform
#    IO in each case when it is ready.
#
#    NB. since select.select returns as soon as _any_ of the IO objects is
#    "ready" (or the timeout occurs), this involves a "busy wait" - i.e. the
#    program busy-waits until IO is ready.
#
#    An alternative to this would be to use the event loop system: see
#    Internet Programming with Python, Ch.3.
#
#    @jireland, Oct. 2017.

import sys, select, tty, termios

## Constants
FIFO_FILENAME = '/tmp/test-select'
