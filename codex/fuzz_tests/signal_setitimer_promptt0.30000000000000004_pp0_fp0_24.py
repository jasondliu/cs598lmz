import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)

# This open() may hang indefinitely
myfile = open("/dev/ttyS0", "r")

# 使用signal.alarm()
import os
import signal

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely
myfile = open("/dev/ttyS0", "r")

signal.alarm(0)          # Disable the alarm

#
