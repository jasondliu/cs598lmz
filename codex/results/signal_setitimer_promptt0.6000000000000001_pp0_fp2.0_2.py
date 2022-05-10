import signal
# Test signal.setitimer
#
# This test should print "signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)"
# every second.  If it doesn't, the test fails.

def handler(signum, frame):
    print "signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)"

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)

# Catch ^C and exit silently.
signal.signal(signal.SIGINT, lambda signum, frame: sys.exit(0))

# Wait forever.
while True: time.sleep(1)
