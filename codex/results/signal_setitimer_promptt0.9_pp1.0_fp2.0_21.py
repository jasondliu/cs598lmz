import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'got SIGALRM'

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.01)
time.sleep(0.5)
signal.setitimer(signal.ITIMER_REAL, 0.01)
time.sleep(0.5)
