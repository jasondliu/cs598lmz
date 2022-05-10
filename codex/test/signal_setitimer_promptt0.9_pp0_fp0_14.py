import signal
# Test signal.setitimer
import sys
import time

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

signal.signal(signal.SIGALRM, alarm_handler)

#
# Test ITIMER_REAL
#
for t in [0.5, 1]:
    signal.setitimer(signal.ITIMER_REAL, t)
