import signal
# Test signal.setitimer() for SIGALRM

import sys
import time

def alarm_handler(signum, frame):
    print("alarm_handler", signum, frame)

signal.signal(signal.SIGALRM, alarm_handler)

print("Setting itimer")
signal.setitimer(signal.ITIMER_REAL, 1.0, 0.5)

while True:
    print("Sleeping for 2 seconds")
    time.sleep(2.0)

print("Done")
