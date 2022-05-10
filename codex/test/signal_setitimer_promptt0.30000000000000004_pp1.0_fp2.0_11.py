import signal
# Test signal.setitimer()
#
# This test is a bit of a hack, because it relies on the fact that the
# testsuite runs the test scripts in a subprocess.  If the testsuite
# is run in a single process, this test will hang.

import signal

def handler(signum, frame):
    pass

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Wait for the signal to be delivered.
signal.pause()

# Check that the signal was delivered.
signal.setitimer(signal.ITIMER_REAL, 0, 0)
