import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Call handler() on SIGALRM
signal.signal(signal.SIGALRM, handler)

# Set an alarm for 5 seconds
signal.setitimer(signal.ITIMER_REAL, 5)

# Do stuff
while True:
    pass
