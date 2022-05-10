import signal
# Test signal.setitimer
# NOTE:
#   This does not properly test the alarm() function. For example, if this
#   test is run on a system that does not support the setitimer() function,
#   but does support the alarm() function, then this test will fail.

import signal
import os

def alarm_received(n, stack):
    print 'Alarm', n
    raise SystemExit

signal.signal(signal.SIGALRM, alarm_received)

# First signal in 0.5 seconds
signal.setitimer(signal.ITIMER_REAL, 0.5)

# Second signal in 1.5 seconds
signal.setitimer(signal.ITIMER_REAL, 1.5)

# This print probably won't happen if we get the signals at the right time
print 'Before pause'

# We should get a signal here, and the signal handler raises SystemExit,
# which is in turn caught by test_support.run_unittest(), causing this
# test to exit.
signal.pause()

print 'After pause'
