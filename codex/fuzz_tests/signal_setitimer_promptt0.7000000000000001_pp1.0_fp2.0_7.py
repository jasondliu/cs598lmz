import signal
# Test signal.setitimer() vs. signal.setitimer(0,0)
import signal, time

def handler(signum, frame):
    print "Got signal", signum
    # Restore handler so that we can catch the next signal
    signal.signal(signum, handler)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(1.5)
signal.setitimer(signal.ITIMER_REAL, 0, 0)
time.sleep(1.5)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(1.5)
