import signal
# Test signal.setitimer
def handler(signum, frame):
    print "Signal handler called with signal", signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now to cause a KeyboardInterrupt, which gets
# handled by the except block.  Try it without the try/except
# block to see what happens.
try:
    while 1: pass
except KeyboardInterrupt:
    print 'KeyboardInterrupt'
finally:
    os.close(fd)
    signal.setitimer(signal.ITIMER_REAL, 0)

# Alternative: signal.alarm(5)
# Alternative: signal.setitimer(signal.ITIMER_REAL, 5, 0)
