import signal
# Test signal.setitimer()

import os
import time
import signal

def handler(signum, frame):
    print('Alarm!')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    print('Tick')
    time.sleep(0.2)

# Test signal.setitimer()

import os
import time
import signal

def handler(signum, frame):
    print('Alarm!')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    print('Tick')
    time.sleep(0.2)

# Test signal.setitimer()

import os
import time
import signal

def handler(signum, frame):
    print('Alarm!')

signal.signal(signal.SIGALRM, handler)

