import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(5)
print('Foo')
signal.alarm(0)          # Disable the alarm

# The open() may hang, but the alarm raises an exception anyway
os.close(fd)

# Test signal.set_wakeup_fd()
import os
import signal
import time
import threading

def signal_handler(num, stack):
    print('Received signal %d in %s' % (num, threading.currentThread()))

signal.signal(signal.SIGUSR1, signal
