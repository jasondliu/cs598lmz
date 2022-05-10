import signal
# Test signal.setitimer, .getitimer, .alarm, and sending SIGALRM for various
# values of the interval.

def handler(signum, frame):
    print('Got SIGALRM')

signal.signal(signal.SIGALRM, handler)

def test(i):
    print(signal.getitimer(signal.ITIMER_REAL))
    signal.setitimer(signal.ITIMER_REAL, i)
    signal.alarm(i)
    p = signal.setitimer(signal.ITIMER_REAL, 0)
    signal.alarm(0)
    print(p)

for i in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5):
    test(i)
