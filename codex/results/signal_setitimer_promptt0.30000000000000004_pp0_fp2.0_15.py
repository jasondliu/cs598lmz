import signal
# Test signal.setitimer
import signal
import time

def handler(signum, frame):
    print("Got signal", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    time.sleep(1)

# Test signal.setitimer
import signal
import time

def handler(signum, frame):
    print("Got signal", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    time.sleep(1)

# Test signal.setitimer
import signal
import time

def handler(signum, frame):
    print("Got signal", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)


