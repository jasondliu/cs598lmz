import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C now

# After 5 seconds, a SIGALRM signal is sent
# and the signal handler is called.  The open()
# call is interrupted, so its exception is raised.

# The exception is caught and the program continues.
# The alarm is disarmed, so it will not fire again.
try:
    tty.setraw(fd)
except select.error, e:
    print 'select.error:', e

# The alarm is still disarmed, so the following
# sleep() call does not raise the exception.
time.sleep(10)

# Press Ctrl+C again, and the handler is called again.
