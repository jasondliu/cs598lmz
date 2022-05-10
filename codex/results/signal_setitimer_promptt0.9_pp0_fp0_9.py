import signal
# Test signal.setitimer on each signal that can have a timer started.
for sig in range(1, signal.NSIG):
    try:
        signal.setitimer(signal.ITIMER_REAL, 0, 1
