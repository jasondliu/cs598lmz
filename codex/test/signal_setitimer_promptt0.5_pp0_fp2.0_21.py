import signal
# Test signal.setitimer()
#
# This test is very timing dependent.  It will only work on a fast computer
# with a fast clock.  It is best to run it on a lightly loaded computer.
#
# It may be necessary to run it several times before it succeeds.
#
# The test passes if the test program exits normally.  If it gets stuck in
# an infinite loop, the test fails.
#
# The test program uses setitimer() to set up a timer to send itself a
# SIGALRM signal every 10 milliseconds.  It then sleeps for 1 second.  It
# counts the number of SIGALRM signals it receives, and exits if it receives
# more than 100.
#
# The test program should receive between 100 and 110 SIGALRM signals.  If it
# receives more than 110, it will get stuck in an infinite loop.  If it
# receives less than 100, the test fails.

# This test is a bit tricky.  We can't use a simple loop and sleep() because
# the sleep() function may interrupt the SIGALRM signal.
#
# Instead, we use a loop and select() with a timeout
