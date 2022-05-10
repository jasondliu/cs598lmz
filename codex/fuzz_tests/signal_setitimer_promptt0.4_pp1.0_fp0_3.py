import signal
# Test signal.setitimer()
#
# This test is not portable.  It depends on the system's timer resolution.
# It also depends on the timer resolution being accurate.
#
# This test is not reliable.  It depends on the system's load.  On a
# heavily loaded system, the timer may not fire at all.
#
# This test is not robust.  It depends on the system's timer resolution
# not changing during the test.  On some systems, the timer resolution
# changes dynamically.
#
# This test is not thorough.  It depends on the system's timer resolution
# being a power of two.  On some systems, the timer resolution is not
# a power of two.
#
# This test is not useful.  It depends on the system's timer resolution
# being less than one second.  On some systems, the timer resolution is
# one second.

import errno
import os
import signal
import sys
import time

def handler(signum, frame):
    global got_alarm
    got_alarm = 1

def test(itimer):
    global got_alarm
    got_al
