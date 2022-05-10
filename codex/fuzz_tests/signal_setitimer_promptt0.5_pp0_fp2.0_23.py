import signal
# Test signal.setitimer()

import signal
import time

def handler(signum, frame):
    print("Got SIGALRM")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

while True:
    time.sleep(1)
    print("tick")
