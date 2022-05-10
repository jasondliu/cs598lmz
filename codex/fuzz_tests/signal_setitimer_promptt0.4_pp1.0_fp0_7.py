import signal
# Test signal.setitimer()
#
# This program uses signal.setitimer() to schedule a SIGALRM signal
# in 1 second, and then prints a message when the signal is received.
#
# The program terminates after printing the message.
#
# This program is a simple demonstration of signal.setitimer() and
# signal.signal().
#
# This program requires Python 2.6 or later.
#

# Function to print a message when the signal is received.
def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 1-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Do other things in the meantime

# When the alarm goes off, a SIGALRM signal is sent, and the handler
# is called.  Note that only one signal is queued, so if the handler
