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

# Restore the old signal handler for SIGALRM
signal.signal(signal.SIGALRM, signal.SIG_DFL)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do some work, and maybe hang out...
time.sleep(10)

# Close the file descriptor
os.close(fd)
