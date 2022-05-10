import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Kaboom")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# This open() may hang indefinitely
#fd = os.open('/dev/ttyS0', os.O_RDWR)

# This open() may hang indefinitely
#fd = os.open('/dev/ttyS0', os.O_RDWR)

# This open() may hang indefinitely
#fd = os.open('/dev/ttyS0', os.O_RDWR)

# This open() may hang indefinitely
#fd = os.open('/dev/ttyS0', os.O_RDWR)

# This open() may hang indefinitely
#
