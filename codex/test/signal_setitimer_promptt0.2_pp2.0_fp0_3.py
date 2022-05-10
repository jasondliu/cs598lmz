import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

print('Continuing')

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do some more work, and save the results
os.write(fd, b'Hello world\n')

# Now we can exit
os.close(fd)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

print('done')
