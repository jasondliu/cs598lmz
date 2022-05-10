import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.setitimer(signal.ITIMER_REAL, 0)
print('Continuing')

# The following code is executed if the try clause does not raise an exception.
# The except clause may specify a variable after the exception name.
# The variable is bound to an exception instance with the arguments stored in instance.args.
# For convenience, the exception instance defines __str__() so the arguments can be printed directly without having to reference .args.
# One may also instantiate an exception first before raising it and add any attributes to it as desired.
try:
    raise Exception('sp
