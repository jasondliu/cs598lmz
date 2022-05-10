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
# with the exception of the open() call, which is interrupted by the
# signal handler.

# The alarm is reset to 5 seconds after the signal handler returns.
# This means that if the open() call hangs, the program will hang for
# 5 seconds, then the signal handler will be called, and the alarm
# will be reset to 5 seconds.

# The program will hang for 5 seconds, then the signal handler will
# be called, and the alarm will be reset to 5 seconds.

# The
