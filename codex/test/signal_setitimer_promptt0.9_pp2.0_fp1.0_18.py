import signal
# Test signal.setitimer()
# This takes 3 arguments: which timer, a timeval for the initial delay, and
# another timeval for the interval. At each interval, a signal is posted.
# With no interval, this acts like alarm(). Each signal causes the timer to
# be re-posted.
# The signal is SIGALRM on Mac OS X, SIGVTALRM on FreeBSD.

# This version does the math in Python instead of C.


def handler(signum, frame):
    print(signum, frame)


signal.signal(signal.SIGALRM, handler)
print('Setting timer')
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.2)
input('Waiting...')
print('Disabling timer')
signal.setitimer(signal.ITIMER_REAL, 0)
input('Waiting...')
print('Done')
