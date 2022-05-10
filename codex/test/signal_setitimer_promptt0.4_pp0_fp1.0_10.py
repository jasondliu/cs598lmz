import signal
# Test signal.setitimer()

def signal_handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

os.write(fd, b'Hello world\n')

# Now read the response
resp = os.read(fd, 1024)

print(resp)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)
