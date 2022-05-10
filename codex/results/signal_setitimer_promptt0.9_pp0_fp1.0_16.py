import signal
# Test signal.setitimer() on POSIX platforms: send a signal every 10 seconds.
# Use signal.setitimer(), signal.getitimer() to reprogram the alarm after each
# signal


def signal_handler(signum, frame):
    print('signal %s at %s' % (signum, time.ctime()))
    signal.setitimer(signal.ITIMER_REAL, 3, 2)

signal.signal(signal.SIGALRM, signal_handler)

signal.setitimer(signal.ITIMER_REAL, 3, 2)

while True:
    # should ignore remaining signal handlers
    signal.pause()
