import signal
# Test signal.setitimer()

# In linux, when the process is the foreground process,
# it does not need to set block false.
signal.signal(signal.SIGALRM, lambda s, f: sys.exit(1))
signal.setitimer(signal.ITIMER_REAL, 3)
time.sleep(5)
