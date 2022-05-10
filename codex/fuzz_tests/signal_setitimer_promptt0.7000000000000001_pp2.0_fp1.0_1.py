import signal
# Test signal.setitimer by setting an alarm and waiting for it to go off.

def handler(signum, frame):
    global got_alarm
    got_alarm = True

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

got_alarm = False
while not got_alarm:
    pass

print "good"

# 1. This test runs in the background for some time.
# 2. In the meanwhile, we can do useful work.
#
# Here we are busy-waiting for a global variable to go from False to True.
# The SIGALRM handler sets the global variable to True.
# This can be used to implement timeouts for long-running operations.
#
# Note that the SIGALRM handler does not interrupt the program
# at a specific point in the code.
# The handler runs in its own context, completely separately from the main thread of the program.

# 3. Check that alarm fires even when there is no main thread.

# The next test is somewhat tricky.
