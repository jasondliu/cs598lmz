import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now!

# After 5 seconds, a SIGALRM signal is sent
# and the handler is called.  The alarm is
# automatically reset (to 5 more seconds), so
# only one signal is sent after waiting 5 seconds.

print 'Sleeping for 10 seconds'
time.sleep(10)

print 'Done'
