import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    "Handler for SIGALRM."
    print 'Got alarm'
    raise RuntimeError

signal.signal(signal.SIGALRM, handler)

t = signal.getitimer(signal.ITIMER_REAL)
print 'Starting timer:', t
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
print 'Sleeping'
time.sleep(0.2)
print 'Sleeping some more'
time.sleep(1)
print 'Done'
