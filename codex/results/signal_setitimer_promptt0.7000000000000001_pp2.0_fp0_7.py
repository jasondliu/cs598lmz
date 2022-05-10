import signal
# Test signal.setitimer()
#
# This test is Linux-only; it relies on the ITIMER_PROF timer,
# which is not supported on any other platform.

import os, signal, time

if signal.setitimer(signal.ITIMER_PROF, 0.5, 0.5) == 0:
    raise ValueError("setitimer() requires an interval")

def handler(signum, frame):
    print "alarm"
    signal.alarm(0)

sigset = signal.siginterrupt(signal.SIGALRM, False)
signal.signal(signal.SIGALRM, handler)

signal.alarm(1)
time.sleep(2)

signal.siginterrupt(signal.SIGALRM, sigset)
print "end"
