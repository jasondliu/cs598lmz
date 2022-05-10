import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Register handler
signal.signal(signal.SIGALRM, handler)

# Define a timeout for your function
signal.setitimer(signal.ITIMER_REAL,0.1)

# Do some work
time.sleep(0.2)

# Disable the timer
signal.setitimer(signal.ITIMER_REAL,0)

# Do some more work
time.sleep(0.2)
