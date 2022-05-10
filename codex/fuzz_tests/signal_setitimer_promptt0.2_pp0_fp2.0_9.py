import signal
# Test signal.setitimer()

def handler(signum, frame):
    print "Signal handler called with signal", signum

# Call handler when a signal is received
signal.signal(signal.SIGALRM, handler)

# Define a 5-second alarm
signal.setitimer(signal.ITIMER_REAL, 5)

# Do stuff
while True:
    print "Doing stuff..."
    time.sleep(1)
</code>

