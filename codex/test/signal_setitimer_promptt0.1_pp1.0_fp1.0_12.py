import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now to send a SIGINT
# Now the alarm signal should be received
# and the handler will be called

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

# Do something else in the meantime
print('Doing other things')
time.sleep(3)

# Close the file descriptor
os.close(fd)

print('Exiting')
