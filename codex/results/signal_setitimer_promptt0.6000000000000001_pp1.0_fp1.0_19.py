import signal
# Test signal.setitimer in Python
#
# This script will be terminated after 10 seconds.
#

def timeout_handler(signum, frame):
    print "Timeout"

# Set up signal handler
signal.signal(signal.SIGALRM, timeout_handler)

# Set up ITIMER_REAL to fire after 10 seconds
signal.setitimer(signal.ITIMER_REAL, 10, 0)

while True:
    pass
