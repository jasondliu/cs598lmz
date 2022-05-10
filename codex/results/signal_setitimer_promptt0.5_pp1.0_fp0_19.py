import signal
# Test signal.setitimer() in Python.
#
# Reference: http://stackoverflow.com/questions/492519/timeout-on-a-function-call
def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL,5)

# This open() may hang indefinitely
#fd = os.open('/dev/ttyS0', os.O_RDWR)

# Restore the old signal handler for SIGALRM
signal.setitimer(signal.ITIMER_REAL,0)

#------------------------------------------------------------------------------
# Test signal.setitimer() in C.
#
# Reference: http://stackoverflow.com/questions/492519/timeout-on-a-function-call
#
# Compile with:
# gcc -o test_signal test_signal.c -Wall -W
