import signal
# Test signal.setitimer used in child-termination-signal-reinit.test

signal.setitimer(signal.ITIMER_REAL, 0, None)
signal.setitimer(signal.ITIMER_PROF, 0, None)
signal.setitimer(signa
