import signal
# Test signal.setitimer() on Linux
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# Test signal.setitimer() on Windows
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
# Test signal.setitimer() on Windows
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

# Test signal.getitimer() on Linux
signal.getitimer(signal.ITIMER_REAL)
# Test signal.getitimer() on Windows
signal.getitimer(signal.ITIMER_VIRTUAL)
# Test signal.getitimer() on Windows
signal.getitimer(signal.ITIMER_PROF)

# Test signal.signal() on Linux
signal.signal(signal.SIGALRM, lambda signum, frame: None)
# Test signal.signal() on Windows
signal.signal(signal.SIGBREAK, lambda signum,
