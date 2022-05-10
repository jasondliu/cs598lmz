import signal
# Test signal.setitimer() with a real timer. It should raise IOError if not
# supported.
try:
    signal.setitimer(signal.ITIMER_REAL, 1)
except IOError as e:
    if "setitimer" in str(e):
        raise TestSkipped("setitimer not supported on this platform")
    raise
