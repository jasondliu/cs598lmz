import signal
# Test signal.setitimer()

# This test is a bit tricky.  It tests the setitimer() function, but the
# test itself is run in a child process.  The child process sets up an
# alarm handler, then sets an alarm using setitimer() and then waits
# for a signal.  The parent process then sends the signal.  The child
# process then verifies that the alarm handler was called.

