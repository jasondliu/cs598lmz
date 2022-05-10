import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C to deliver a SIGINT
# Press Ctrl+\ to deliver a SIGQUIT
# Press Ctrl+Z to deliver a SIGTSTP

# Now do some time consuming work so you have
# a chance to see the signal arrive
c = ''
while c != '\n':
    c = os.read(fd, 1)
    print 'Read %d character' % len(c)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)
