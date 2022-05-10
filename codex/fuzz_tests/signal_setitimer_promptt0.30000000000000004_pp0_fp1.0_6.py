import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Signal handler called with signal", signum

# Call handler when SIGALRM arrives
signal.signal(signal.SIGALRM, handler)

# Set an alarm for 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# Do some busy work
while True:
    pass
