import signal
# Test signal.setitimer()
# It should be available on Linux, but not Windows
# https://docs.python.org/2/library/signal.html#signal.setitimer
# http://stackoverflow.com/questions/4807258/signal-setitimer-does-not-exist
import time
import os
import math
import cmath

def signal_handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL,5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm
print "fd is",fd

# https://github.com/szazo/DHT11_Python
import dht11
import RPi.GPIO as GPIO


