import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C to deliver a signal and execute the signal handler
# Press Ctrl+Z to stop the process and execute the signal handler
# Press Ctrl+\ to deliver a SIGQUIT signal and core dump the process

# After the alarm fires, read() returns 0 bytes available
os.read(fd, 100)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Close the file
os.close(fd)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Close the file
os.close(fd)
