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

# Now I can do other things here, and eventually read or write
# the serial port

# When the alarm goes off, a SIGALRM signal is sent to the process,
# and the signal handler is executed.

# The open() call is interrupted, and an exception is raised.

# The exception is handled, the alarm is reset, and the open() call
# is tried again.

# This continues until the device is successfully opened.


