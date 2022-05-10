import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL,2,1)
signal.signal(signal.SIGALRM,handler)

