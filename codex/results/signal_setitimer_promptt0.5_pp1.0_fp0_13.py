import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Call handler when a signal is received
signal.signal(signal.SIGALRM, handler)

# Define a 5-second alarm
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

print 'Signal handler returned'
print 'All done'
