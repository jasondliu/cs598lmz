import signal
# Test signal.setitimer

import signal

def handler(signum, frame):
    print("handler")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass
