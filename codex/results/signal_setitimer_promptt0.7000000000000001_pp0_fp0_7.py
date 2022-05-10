import signal
# Test signal.setitimer to verify that it works
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)
# The signal handler.
def handler(signum, frame):
    print "Timer expired", frame
    # Don't schedule another signal
    signal.setitimer(signal.ITIMER_REAL, 0)
# Register the handler
signal.signal(signal.SIGALRM, handler)

# Do something repeatedly
while True:
    print "foo"
    time.sleep(0.1)
