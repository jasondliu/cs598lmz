import signal
# Test signal.setitimer()
#
# The test is done by setting an alarm signal handler and then
# setting an interval timer.  The interval timer should interrupt
# the sleep() call.
#
# Note that this test will fail if the sleep() call is interrupted
# by any other signal (e.g., keyboard interrupt).

