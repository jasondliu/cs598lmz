import signal
# Test signal.setitimer
#
# This test is a bit tricky.  The test will run for a few seconds,
# then the timer will fire and the test will exit.  The timer is
# set to fire every second.  The test will check that the timer
# fired at least twice.

