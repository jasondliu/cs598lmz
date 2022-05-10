import signal
# Test signal.setitimer()

# Callback function
def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Register handler for SIGALRM
signal.signal(signal.SIGALRM, handler)

# Define a timeout for alarm
signal.setitimer(signal.ITIMER_REAL, 2)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do some more work, and save our progress periodically in case we
# get interrupted again.
while True:
    pass
