import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now to send a SIGINT before the alarm goes off

# After the alarm, a SIGALRM is sent and the signal handler is called
# with the exception that interrupts the open()

# Now the open() returns with an error
print("Continuing")

# The alarm is still set, so another SIGALRM will be sent in 5 seconds

# Press Ctrl+C again to send a SIGINT and interrupt the sleep()
time.sleep(10)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# The sleep() is interrupted, so the program continues
