import signal
# Test signal.setitimer
import os
import time

def handler(signum, frame):
    print('received signal', signum, frame)
    if signum == signal.SIGALRM:
        os.kill(os.getpid(), signal.SIGALRM)

oldhandler = signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(0.5)
