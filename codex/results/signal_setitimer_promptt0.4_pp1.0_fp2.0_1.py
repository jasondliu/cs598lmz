import signal
# Test signal.setitimer() and signal.getitimer()

import signal
import time

def handler(signum, frame):
    raise RuntimeError

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(2)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

# Test signal.setitimer() and signal.getitimer()

import signal
import time

def handler(signum, frame):
    raise RuntimeError

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(2)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

# Test signal.setitimer() and signal.getitimer()

import signal
import time

def handler(signum, frame):
    raise RuntimeError
