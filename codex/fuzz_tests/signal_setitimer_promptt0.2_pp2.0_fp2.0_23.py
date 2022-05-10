import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Register the signal function handler
signal.signal(signal.SIGALRM, handler)

# Define a timeout for your function
signal.setitimer(signal.ITIMER_REAL, 0.1)

# This will run until the timer goes off
while True:
    pass
