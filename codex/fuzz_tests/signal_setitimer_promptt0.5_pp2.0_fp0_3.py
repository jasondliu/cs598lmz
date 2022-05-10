import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Alarm!'

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2, 0)
while True:
    pass
