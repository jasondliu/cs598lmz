import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

print('Yay!')

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do some more work, and save the results
os.write(fd, b'Hello world\n')

# Now we can exit
os.close(fd)

# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIM
