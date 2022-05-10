import signal
# Test signal.setitimer(signal.ITIMER_REAL, 0, 1)
# For some reason it doesn't work.
# See http://bugs.python.org/issue1528894

# Here's how it's intended to work:
# send SIGALRM every 1 second
signal.setitimer(signal.ITIMER_REAL, 0, 1)

# Send SIGUSR1 at 1.5 seconds
signal.setitimer(signal.ITIMER_REAL, 0.5, 1)

def handler(signum, frame):
    print("SIGALRM handler")
    print("Last time: {0}".format(time.time()))

signal.signal(signal.SIGALRM, handler)

def handler2(signum, frame):
    print("SIGUSR1 handler")
    print("Last time: {0}".format(time.time()))
    signal.setitimer(signal.ITIMER_REAL, 0, 1)

