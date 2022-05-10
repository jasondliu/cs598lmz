import signal
# Test signal.setitimer() on SVR4 with BSD 4.3-compatible semantics.
# This tests the BSD 4.3-compatible semantics and not the SVR4 semantics.
# This requires the particular setup described in the comment at the end
# of this file.  (This test is known to fail if the time.sleep() call
# is replaced with a time.select() call.)

# The test creates two process: a parent and a child.  The child installs
# a handler that catches SIGALRM signals and exits when it receives 3
# SIGALRM signals.  The parent then sets up an interval timer to deliver
# SIGALRM signals every 1.5 seconds and waits for the child to exit.

# This test is known to fail on the following systems:

# SunOS 4.1.3:
#   The parent receives a SIGALRM signal after about 80 seconds,
#   even though the interval timer was set up for 1.5 seconds.
#   The child also receives 3 SIGALRM signals.

# Solaris 2.4:
#   The parent receives a SIGALRM signal after about 86 seconds,
#   even though
