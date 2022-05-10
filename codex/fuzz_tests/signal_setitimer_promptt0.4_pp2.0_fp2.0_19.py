import signal
# Test signal.setitimer
import time
import sys

def handler(signum, frame):
    print "Got signal", signum

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.3, 0.2)

# Wait for the alarm
time.sleep(1)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Wait for another alarm
time.sleep(1)

# Enable the alarm
signal.setitimer(signal.ITIMER_REAL, 0.3, 0.2)

# Wait for another alarm
time.sleep(1)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Wait for another alarm
time.sleep(1)

# Enable the alarm
signal.setitimer(signal.ITIMER_REAL, 0.3, 0.2)

# Wait for another alarm
time.sleep(1)

