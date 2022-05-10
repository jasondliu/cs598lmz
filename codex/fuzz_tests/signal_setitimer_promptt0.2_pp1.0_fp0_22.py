import signal
# Test signal.setitimer()
#
# This test is a bit tricky.  It uses the SIGALRM signal to
# implement a timer.  The timer is set to go off in a few seconds,
# and the test waits for the timer to go off.  If the timer goes off,
# the test passes.  If the timer doesn't go off, the test fails.
#
# The tricky part is that the test needs to be able to handle the
# timer going off while the test is running.  If the timer goes off
# while the test is running, the test will fail.  To avoid this, the
# test installs a signal handler for SIGALRM that simply sets a flag
# to indicate that the timer went off.  The test then checks the flag
# after the timer is set to see if the timer went off before the test
# was run.  If the timer went off before the test was run, the test
# fails.
#
# The test also needs to be able to handle the timer going off while
# the signal handler is running.  If the timer goes off while the
# signal handler is running, the test will fail.  To avoid this
