import signal
# Test signal.setitimer() on Linux
# (it is not supported on FreeBSD)

def signal_handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
print(open('/dev/ttyS0', 'rb'))
 
# After 5 seconds, a SIGALRM signal is sent
# and the signal handler will get called.
# The open() call will be interrupted and
# an IOError exception will be raised.

# Using a timeout with select()
#
# The select() function is a direct interface to the Unix select() system call.
# It can be used to monitor multiple file descriptors to see if I/O is possible
# on any of them. It can also be used to wait for a timeout period to elapse.
# The function has no additional semantics, beyond what is described in the
# Unix manual.
#
import
