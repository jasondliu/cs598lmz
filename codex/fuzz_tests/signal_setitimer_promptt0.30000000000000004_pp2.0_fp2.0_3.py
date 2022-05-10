import signal
# Test signal.setitimer()

import signal

def handler(signum, frame):
    print("Alarm")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

signal.pause()
