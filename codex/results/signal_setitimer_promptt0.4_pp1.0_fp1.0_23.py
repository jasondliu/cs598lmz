import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

def handler(signum, frame):
    print "Signal handler called with signal", signum
    raise IOError("Couldn't open device!")

signal.signal(signal.SIGALRM, handler)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Install the alarm handler
signal.alarm(10)

# This read may hang indefinitely
os.read(fd, 1)

# Disable the alarm
signal.alarm(0)

# Do some more work, and save the results.
# ...

# Re-enable the alarm
signal.alarm(10)

# Do some more work, and save the results.
# ...

# Disable the alarm
signal.alarm(0)

# Restore the previous signal handler
signal.signal(signal.SIGALRM, old_handler)
