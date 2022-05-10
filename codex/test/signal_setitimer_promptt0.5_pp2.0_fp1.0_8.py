import signal
# Test signal.setitimer()

import os
import time
import signal

def handler(signum, frame):
    print('Alarm :', time.ctime())
    raise IOError("getcwd: '.'")

try:
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    print('Before:', time.ctime())
    cwd = os.getcwd()
    print('After :', time.ctime())
except IOError as err:
    print('Got', err)
else:
    print('No error!')

signal.setitimer(signal.ITIMER_REAL, 0)

# Test signal.setitimer()

import os
import time
import signal

def handler(signum, frame):
    print('Alarm :', time.ctime())
    raise IOError("getcwd: '.'")

