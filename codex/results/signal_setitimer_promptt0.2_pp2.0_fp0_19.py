import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+c to deliver a SIGINT to the process, and check the handler
# was called
signal.pause()

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do some work, and check the handler was not called
time.sleep(10)

# Restore the old signal handler
signal.signal(signal.SIGALRM, signal.SIG_DFL)
