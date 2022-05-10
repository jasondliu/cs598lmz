import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

# This open() may hang indefinitely
fd = os.open('somefile.txt', os.O_RDONLY)

# After 1 second, a SIGALRM signal is sent
# Our signal handler prints a message
# Note that the alarm() is reset after this signal handler returns

# This open() may hang indefinitely again
fd = os.open('somefile.txt', os.O_RDONLY)

# Set the signal handler and a 5-second alarm again
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

# This open() may hang indefinitely again
fd = os.open('somefile.txt', os.O_RDONLY)

# After 1
