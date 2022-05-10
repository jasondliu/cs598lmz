import signal
# Test signal.setitimer()
# This test is not very good, because it is difficult to test that
# the timer is actually working.

# This test is Linux specific.

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
