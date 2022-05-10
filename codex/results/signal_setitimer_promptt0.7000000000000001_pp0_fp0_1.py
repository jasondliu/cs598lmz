import signal
# Test signal.setitimer()

# This test needs to be run under a timeout (e.g. with the 'timeout'
# program), otherwise it may lock up.  If it locks up, either the
# test or the implementation is broken.

def handler(signum, frame):
    print "handler"

signal.signal(signal.SIGALRM, handler)

# We set the interval to 2 seconds here because the test runner uses
# a 1 second timeout.
signal.setitimer(signal.ITIMER_REAL, 2, 2)

time.sleep(10)

print "test finished"
