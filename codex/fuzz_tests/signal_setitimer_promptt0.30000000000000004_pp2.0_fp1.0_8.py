import signal
# Test signal.setitimer()
#
# This test is a bit tricky because setitimer() is not guaranteed to
# be accurate to the microsecond.  So we set the timer to a value
# that's large enough that we can be reasonably sure it won't expire
# before we want it to.

def handler(signum, frame):
    print("handler")
    raise SystemExit

signal.signal(signal.SIGALRM, handler)

# Set the timer to expire in 1 second
signal.setitimer(signal.ITIMER_REAL, 1.0)

# Wait for the timer to expire
while True:
    pass
