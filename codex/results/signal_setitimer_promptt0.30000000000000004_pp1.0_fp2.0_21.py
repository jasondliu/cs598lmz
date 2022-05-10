import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# # Disable the alarm
# signal.setitimer(signal.ITIMER_REAL, 0)

# Do stuff with fd

# # Re-enable the alarm
# signal.setitimer(signal.ITIMER_REAL, 5)

# Do more stuff with fd

# # Disable the alarm again
# signal.setitimer(signal.ITIMER_REAL, 0)

# Close the file descriptor
os.close(fd)

# # Re-enable the alarm
# signal.setitimer(signal.ITIMER_REAL, 5)

# Do stuff


