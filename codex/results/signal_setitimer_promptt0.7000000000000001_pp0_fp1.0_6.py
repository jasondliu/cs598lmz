import signal
# Test signal.setitimer()

def sigalrm_handler(signum, frame):
    print 'SIGALRM received'
    raise KeyboardInterrupt

signal.signal(signal.SIGALRM, sigalrm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)

try:
    while True:
        pass
except KeyboardInterrupt:
    print 'KeyboardInterrupt received'
print 'Exiting'

# Test signal.setitimer(signal.ITIMER_VIRTUAL)

def sigvtalrm_handler(signum, frame):
    print 'SIGVTALRM received'
    raise KeyboardInterrupt

signal.signal(signal.SIGVTALRM, sigvtalrm_handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.5)

try:
    while True:
        pass
except KeyboardInterrupt:
    print 'KeyboardInterrupt received'
print 'Exiting'
