import signal
# Test signal.setitimer() on SIGVTALRM and SIGPROF.
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.2)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.2)

# Test signal.getitimer() on SIGVTALRM and SIGPROF.
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)

# Test signal.getitimer() with non-existent timer.
try:
    signal.getitimer(-1)
except ValueError as e:
    if str(e) != 'signal number out of range':
        raise

# Test signal.getitimer() with invalid signal.
try:
    signal.getitimer(signal.SIGCHLD)
except ValueError as e:
    if str(e) != 'signal only works for real-time signals in timer mode':
        raise

# Test signal.setitimer() with non-existent timer
