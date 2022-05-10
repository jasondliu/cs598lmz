import signal
# Test signal.setitimer() and signal.getitimer()

import time

def handler(signum, frame):
    print("Got alarm", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.2)
signal.setitimer(signal.ITIMER_REAL, 0)
time.sleep(0.2)
print(signal.getitimer(signal.ITIMER_REAL))
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)
time.sleep(0.2)
print(signal.getitimer(signal.ITIMER_REAL))
time.sleep(0.2)
print
