import signal
# Test signal.setitimer() on GIL non-release platforms.
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.2)
def handler(sig, frame):
    print("handler", sig)
signal.signal(signal.SIGALRM, handler)
time.sleep(0.2)

# test setitimer() before signal.signal() was installed.
signal.setitimer(signal.ITIMER_REAL, 0, 0)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.2)
signal.signal(signal.SIGALRM, handler)
time.sleep(0.2)

signal.setitimer(signal.ITIMER_REAL, 0, 0)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.2)
signal.signal(signal.
