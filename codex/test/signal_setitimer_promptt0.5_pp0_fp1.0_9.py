import signal
# Test signal.setitimer() by registering a signal handler that
# increments a counter.

signal.alarm(1)

def handler(signum, frame):
    global n
    n += 1
    signal.setitimer(signal.ITIMER_REAL, 0.1)

n = 0
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

while n < 10:
    pass

