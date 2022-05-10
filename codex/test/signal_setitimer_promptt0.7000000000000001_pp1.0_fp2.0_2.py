import signal
# Test signal.setitimer fails with bad argument
try:
    signal.setitimer('ITIMER_REAL', 0)
except TypeError:
    print('SKIP')
    raise SystemExit

timer = signal.ITIMER_REAL

# Certain combinations of interval and value are invalid,
# and will cause an OSError.
# These are currently checked by the C implementation of setitimer.
# We skip the tests for these invalid combinations.

skip = [(signal.ITIMER_REAL, 0, 1), (signal.ITIMER_PROF, 0, 1),
        (signal.ITIMER_VIRTUAL, 0, 1), (signal.ITIMER_REAL, 0, 0),
        (signal.ITIMER_PROF, 0, 0), (signal.ITIMER_VIRTUAL, 0, 0)]
try:
    signal.setitimer(timer, 0, 0)
except OSError:
    # On some systems this is not allowed
    skip.append((timer, 0, 0))

