import signal
# Test signal.setitimer()
# Run this program, then in another window do "kill -ALRM <pid>"
# where <pid> is the process ID of this program.

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.setitimer(signal.ITIMER_REAL, 0)
print 'Continuing'

#This is just a test
#This is just a test
#This is just a test
#This is just a test
#This is just a test
#This is just a test
#This is just a test
#This is just a test
#This is just a test
#This is just a test
#This is just a test

