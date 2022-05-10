import signal
# Test signal.setitimer()
def handler(signum, frame):
    print 'Got signal'
    signal.setitimer(signal.ITIMER_VIRTUAL, 0)

signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.3, 0)
while True:
    print 'Woo!'
    time.sleep(1)
'''

# Test signal.setitimer() (2)
'''
def handler(signum, frame):
    print 'Got signal', signum

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)
while True:
    print 'Woo!'
    time.sleep(1)
'''

# Test signal.setitimer() (3)
def handler(signum, frame):
    print 'Got signal', signum

signal.signal(signal.SIGVTALRM, handler)
signal.
