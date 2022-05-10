import signal
# Test signal.setitimer and signal.getitimer
# See if SIGILL is generated:
signal.signal(signal.SIGILL, signal.SIG_IGN)
signal.setitimer(signal.ITIMER_REAL, 0, 1)
signal.getitimer(signal.ITIMER_REAL)
signal.setitimer(signal.ITIMER_VIRTUAL, 0, 1)
signal.getitimer(signal.ITIMER_VIRTUAL)
'''

# Just check that setting these to a value larger than the max doesn't blow
# up
signal.setitimer(signal.ITIMER_REAL, sys.maxint, sys.maxint)
signal.setitimer(signal.ITIMER_VIRTUAL, sys.maxint, sys.maxint)
signal.setitimer(signal.ITIMER_PROF, sys.maxint, sys.maxint)

# Setting a handler for a signal that cannot be caught or ignored should
# cause a RuntimeError
try:
    signal.
