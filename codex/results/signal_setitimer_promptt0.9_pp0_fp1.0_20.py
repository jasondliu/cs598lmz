import signal
# Test signal.setitimer for SIGVTALRM vs. SIGALRM
# (used by the ever-useful 'timeout' bash utility).

# Sanity check that SIGALRM actually works
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

if signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0):
    print "SIGVTALRM OK"
else:
    print "SIGVTALRM FAILED!"

signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)
