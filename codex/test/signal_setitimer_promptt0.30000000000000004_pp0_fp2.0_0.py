import signal
# Test signal.setitimer()
#
# This test is a little tricky because we have to set up a signal handler
# that will do the test and then raise an exception.  The exception is
# caught by the test framework, which then checks the global variable
# "signalled" to see if the test passed.

signalled = False

def handler(signum, frame):
    global signalled
    signalled = True

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# The signal should arrive before the sleep finishes:
time.sleep(1.0)

if not signalled:
    raise AssertionError("setitimer() failed")

# The signal should not arrive while we're sleeping:
signalled = False
time.sleep(0.1)
if signalled:
    raise AssertionError("setitimer() failed")

# The signal should arrive after we wake up:
time.sleep(0.5)
