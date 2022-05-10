import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print("Alarm!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Now set another alarm
signal.setitimer(signal.ITIMER_REAL, 1)

# Do some lengthy stuff
time.sleep(10)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)
os.close(fd)
