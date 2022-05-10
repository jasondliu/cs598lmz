import signal
# Test signal.setitimer()

# Set up a signal handler.
def handler(signum, frame):
    print "got itimer signal", signum
signal.signal(signal.SIGALRM, handler)

# Set itimer.
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

# Wait for signals.
while 1:
    signal.pause()
