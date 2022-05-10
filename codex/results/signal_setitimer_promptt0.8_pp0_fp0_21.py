import signal
# Test signal.setitimer and signal.getitimer.
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
signal.setitimer(signal.ITIMER_PROF, 1, 0)
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)
try:
    signal.setitimer(10, 1, 0)
except ValueError as e:
    print(e)
try:
    signal.getitimer(10)
except ValueError as e:
    print(e)

# Test signal.set_wakeup_fd.
# Issue #21243: wakeup_fd must be non-negative.
try:
    signal.set_wakeup_fd(-1)
except ValueError as e:
    print(e)

# Test resize of handler lists
# First put
