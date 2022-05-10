import signal
# Test signal.setitimer()
#
# This test is derived from test_signal.py, but with the setitimer()
# calls removed.
#
# This test should be run in the background, and then it should be
# killed with SIGALRM.  It should print "ok" before it exits.

