import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.setitimer(signal.ITIMER_REAL, 0)
print('Continuing')

# The following is not strictly necessary, since the alarm is one-shot,
# but it does demonstrate how to turn off the alarm
signal.alarm(0)

# Now do some lengthy stuff
time.sleep(10)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do some more stuff
time.sleep(5)

# Disable the alarm
signal.setitimer(sign
