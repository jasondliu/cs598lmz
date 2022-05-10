import signal
# Test signal.setitimer

import time

def handler(signum, frame):
    print("signal", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

for i in range(5):
    print("sleeping", i)
    time.sleep(0.5)

signal.setitimer(signal.ITIMER_REAL, 0)
