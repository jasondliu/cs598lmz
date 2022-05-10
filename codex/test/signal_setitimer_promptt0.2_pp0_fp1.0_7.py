import signal
# Test signal.setitimer()
#
# This test is a bit tricky, because we need to make sure that the
# signal handler is called before the itimer expires.  We do this by
# setting the itimer to a very short time, and then making sure that
# the signal handler is called before the itimer expires.

