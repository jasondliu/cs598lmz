import signal
# Test signal.setitimer components

import time

def handle_alarm(signum, frame):
    print 'Alarm!'

signal.signal(signal.SIGALRM, handle_alarm)
signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.2)
for i in range(1, 10):
    print 'Sleeping', i
    time.sleep(1)
# Absolute time-based alarms:
print 'Once'
signal.setitimer(signal.ITIMER_REAL, 1.0)
time.sleep(2)
print 'Once'
signal.setitimer(signal.ITIMER_REAL, 1.0)
time.sleep(2)
print 'Once'
signal.setitimer(signal.ITIMER_REAL, 1.0)
time.sleep(2)

def handle_prof(signum, frame):
    print 'Prof!'

signal.signal(signal.
