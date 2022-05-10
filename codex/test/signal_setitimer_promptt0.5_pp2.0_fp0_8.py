import signal
# Test signal.setitimer
#
# This test is not meant to be run standalone.  It is run from test_signal.py
# via the test_itimer() function.
#
# This test uses SIGALRM to test the interval timer.  If the test is run
# on a system that does not support SIGALRM, then it will be skipped.

# This is a list of the tests we will run.  Each test is a tuple of
# (itimer, signal, expected_signal, expected_itimer).  The itimer is the
# itimer to set.  The signal is the signal that we expect to receive.
# The expected_signal is the signal we expect to see in the siginfo
# structure.  The expected_itimer is the itimer we expect to see in the
# siginfo structure.

