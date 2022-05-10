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
# with the exception that interrupts the open() call

# Now the open() call will complete (perhaps after another signal)
os.write(fd, b'Greetings, program!\n')

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Press Ctrl+C again and notice the difference

# Close the file descriptor
os.close(fd)

# Disable the alarm
signal.setitimer(signal.IT
