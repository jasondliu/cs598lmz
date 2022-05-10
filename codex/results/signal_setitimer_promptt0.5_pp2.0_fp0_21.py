import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Handler called with signal", signum)
    raise OSError("Couldn't open device!")

# Call handler when a signal is received
signal.signal(signal.SIGALRM, handler)

# Define a timeout for 'read()'
signal.setitimer(signal.ITIMER_REAL,0.1)

# This will run until the timer goes off
readline.readline()

# Disable the timer
signal.setitimer(signal.ITIMER_REAL,0)
