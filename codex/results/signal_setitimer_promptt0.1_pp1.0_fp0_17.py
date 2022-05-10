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

# The alarm signal will be delivered if the open()
# takes more than 5 seconds

# After the alarm signal, the handler is called
# and the open() is interrupted.

# The alarm signal will also be delivered if the
# process receives a signal, such as SIGINT,
# before the 5 seconds have elapsed.

# The alarm signal will *not* be delivered if the
# process is suspended, for example by a call to
# os.system() that runs a process that does not
#
