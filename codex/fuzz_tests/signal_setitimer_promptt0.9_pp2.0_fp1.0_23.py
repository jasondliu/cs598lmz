import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0, 1)
print "Set itimer Real timer for 0 seconds"
signal.pause()
print "pause"



# Sigaction
import signal

def handler(signum, frame):
    print "Signal handler called with signal", signum
    raise IOError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm
print 'Doing stuff....'
os.close(fd)
print 'Done'
