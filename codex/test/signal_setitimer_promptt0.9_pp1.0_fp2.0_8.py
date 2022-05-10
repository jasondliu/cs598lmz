import signal
# Test signal.setitimer/setitimer breaks during module import.
# See bug #1217750 (Posix)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
