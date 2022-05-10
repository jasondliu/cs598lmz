import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now to send a signal

# After 5 seconds, a SIGALRM signal is sent
# and the signal handler is called.  The open()
# call is interrupted, and an exception is raised.

# A try/finally clause is used to close the file, even
# if the open() call is interrupted by an exception,
# or the program is ended by Ctrl+C.

try:
    print 'Press Return to exit'
    ret = sys.stdin.readline()
finally:
    os.close(fd)

print 'Exited'
