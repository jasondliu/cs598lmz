import signal
# Test signal.setitimer()

def first_handler(signum, frame):
    print 'handler 1'

def second_handler(signum, frame):
    print 'handler 2'

def third_handler(signum, frame):
    print 'handler 3'
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, first_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.signal(signal.SIGALRM, second_handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
signal.signal(signal.SIGALRM, third_handler)
time.sleep(2)
