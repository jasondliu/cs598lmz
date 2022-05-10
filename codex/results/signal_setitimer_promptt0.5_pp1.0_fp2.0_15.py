import signal
# Test signal.setitimer()
#
# This test is supposed to be run by a process that catches SIGALRM.
#
# When run, this test repeatedly sets an alarm for a short time in the
# future, then sleeps for a longer time.  The test passes if it wakes
# up exactly once for each alarm it sets.

import os, sys, time

# How long to sleep between alarms
SLEEPTIME = 0.5

# How long to sleep between the alarm and the first SIGALRM
WAITTIME = 0.2

# How long the alarm should be set for
ALARMTIME = 0.1

# How long to sleep between each SIGALRM
ALARMPAUSE = 0.1

def handler(signum, frame):
    global count, alarmtime, sleeptime
    print "Signal handler invoked with signal", signum
    if signum != signal.SIGALRM:
        os._exit(1)
    count = count + 1
    alarmtime = alarmtime + ALARMPAUSE
    signal.setitimer(signal.ITIMER_REAL, alarmtime)

