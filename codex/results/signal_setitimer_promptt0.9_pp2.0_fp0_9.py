import signal
# Test signal.setitimer
#
# This testcase tests that the setitimer() function works for
# process-directed timers (e.g. it_value != 0, it_interval = 0) by
# letting the testcase sleep for a few seconds, print "." first and last
# and finally sleeping for a few more seconds and dying.
#
# This test was written with the intention of testing interrupts of sleep
# calls; it should be converted to something like a 5 second sleep and a few
# kills in between as soon as there is a way to check whether sleep is
# interrupted by a signal and thus returns early.

import time
import unittest
from test import test_support

# Test that signals ACTUALLY interrupt sleep
#
# On Unix, SIGSTOP and SIGCONT can be delivered to the process itself,
# just like they can be to any other process. If they are, they will wake
# up the process. Don't ask me why.
#
# This test is to make sure that sleep actually gets the wakeup call when
# signals are sent to us.
#
# The theory behind this test is that after sending signals to
