import signal
# Test signal.setitimer()
#
# This test is designed to be run in the background.
# It will terminate after a few seconds.
#
# The test will print "ok" if it succeeds, or "not ok" if it fails.
#
# If the test fails, it will print out the reason for the failure.
#
# The test will not produce any output if it succeeds.

# Set up a signal handler for SIGALRM
def handler(signum, frame):
    print("not ok 1 - setitimer() test")
    print("# SIGALRM not received")
    sys.exit(1)

signal.signal(signal.SIGALRM, handler)

# Set the timer to go off in 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# Wait for the alarm to go off
signal.pause()

# If we get here, the test has failed
print("not ok 1 - setitimer() test")
print("# SIGALRM not received")
