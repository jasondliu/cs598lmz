import signal
# Test signal.setitimer()
#
# The test is done by setting an alarm signal handler and then
# setting an interval timer.  The interval timer should interrupt
# the sleep() call.
#
# Note that this test will fail if the sleep() call is interrupted
# by any other signal (e.g., keyboard interrupt).

def handler(signum, frame):
    print "caught alarm"

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
time.sleep(1)
print "slept 1 second"
time.sleep(1)
print "slept 1 second"
signal.setitimer(signal.ITIMER_REAL, 0, 0)
time.sleep(1)
print "slept 1 second"
