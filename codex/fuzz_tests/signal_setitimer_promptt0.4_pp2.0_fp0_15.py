import signal
# Test signal.setitimer()
def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Now set another alarm
signal.setitimer(signal.ITIMER_REAL, 5)

# And do some more work, maybe even open /dev/ttyS0 again

# When the alarm goes off, a signal is sent and the signal handler runs
# The alarm is reset to 5 more seconds
# When the alarm goes off again, the process dies

# If the process dies, it is because of the signal, not because it
# reached the end of the script.

# The signal handler does not get executed when the process dies, so
# any cleanup actions specific to the signal would not get executed.

# To avoid this, we can set
