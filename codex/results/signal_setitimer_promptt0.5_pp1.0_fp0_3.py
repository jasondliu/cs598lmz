import signal
# Test signal.setitimer()

# Check that SIGALRM is not ignored.
signal.signal(signal.SIGALRM, lambda signum, frame: None)

# Check that SIGALRM is generated.
signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.pause()
