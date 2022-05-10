import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('Done')
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.pause()

# A real-world example.

import signal
import time
import urllib.request

def receive_alarm(signum, stack):
    print('Alarm :', time.ctime())

signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(5)

# This will cause the program to exit in 5 seconds
# signal.alarm(0)

print('Before:', time.ctime())
time.sleep(2)
print('After:', time.ctime())

# Here's a similar example that uses a signal handler and alarm to
# implement a timeout on a web connection.

import signal
import urll
