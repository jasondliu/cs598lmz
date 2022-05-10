import signal
# Test signal.setitimer
# This test is Linux-specific.

import signal

def handler(signum, frame):
    print("handler", signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)
signal.pause()
