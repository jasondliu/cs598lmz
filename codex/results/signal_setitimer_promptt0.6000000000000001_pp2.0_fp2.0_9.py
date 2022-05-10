import signal
# Test signal.setitimer

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

def handler(signum, frame):
    print 'handler'

signal.signal(signal.SIGALRM, handler)

while 1:
    pass
