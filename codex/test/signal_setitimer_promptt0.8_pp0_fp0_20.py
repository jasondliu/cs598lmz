import signal
# Test signal.setitimer
#
# This script implements a timer which periodically prints the current date and
# time.
#
# The call `signal.setitimer(signal.ITIMER_REAL, interval, interval)` starts a
# timer which sends a SIGALRM signal every interval seconds. The signal handler
# for SIGALRM is set to `signal_handler` by a call to `signal.signal`.
#
# The call `signal.setitimer(signal.ITIMER_REAL, 0, 0)` stops the timer.
#
# Note that the timer must be reset after each signal.

def signal_handler(signum, frame):
    log.info('sigalrm: date: {0}'.format(time.ctime()))
    signal.setitimer(signal.ITIMER_REAL, 5, 5)

signal.signal(signal.SIGALRM,signal_handler)
signal.setitimer(signal.ITIMER_REAL, 5, 5)

