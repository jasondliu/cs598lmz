import signal
# Test signal.setitimer() by installing and raising a signal:

def signal_handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)
print '''
In this example, the signal handler was installed with the signal.signal() 
function and the alarm was set with signal.setitimer(). The second argument 
of signal.setitimer() is the number of seconds to wait before sending a signal.
The third argument is the timer interval. When the first timer expires, a signal 
is sent and the next timer countdown begins. A value of zero as the second argument 
dis
