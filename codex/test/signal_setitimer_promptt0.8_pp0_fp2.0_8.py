import signal
# Test signal.setitimer.
def handler(a, b):
    print('Got signal %s' % a)
    print(b)
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
while True:
    print(1)
