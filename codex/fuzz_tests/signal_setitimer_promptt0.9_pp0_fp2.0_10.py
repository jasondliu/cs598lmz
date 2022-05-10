import signal
# Test signal.setitimer(signal.ITIMER_REAL, 0)
# without SIGALRM handler set.
# It should not die with SIGFPE.
signal.setitimer(signal.ITIMER_REAL, 0)
