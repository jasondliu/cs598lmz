import signal
# Test signal.setitimer(ITIMER_REAL, 0, 0) as this is used by termios.tcdrain (see issue #17548)
old_handler = signal.signal(signal.SIGALRM, lambda signum, frame: None)
signal.setitimer(signal.ITIMER_REAL, 0, 0)
signal.signal(signal.SIGALRM, old_handler)
