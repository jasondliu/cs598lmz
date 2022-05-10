import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now to deliver the signal

# After the signal is delivered, the following
# is not executed until the signal handler returns
os.write(fd, 'Hello world\n')
os.close(fd)

# Now we are back to the main program
print('Continuing')
