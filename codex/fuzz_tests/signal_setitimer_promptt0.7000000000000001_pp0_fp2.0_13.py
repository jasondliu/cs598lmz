import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_PROF, 1.0)
signal.setitimer(signal.ITIMER_REAL, 2.0)
signal.setitimer(signal.ITIMER_VIRTUAL, 3.0)

def handler(signum, frame):
    print 'Received', signum

signal.signal(signal.SIGPROF, handler)
signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)

while True:
    pass
