import signal
# Test signal.setitimer()
#
# Try to send a signal after a delay, and before the delay.
#
# This test will fail if the delay is too short.

# setitimer() is only available on Unix.
# Skip this test on non-Unix.
import sys
if sys.platform[:3] == 'win':
    print('Test skipped: setitimer() is not available on Windows')
    sys.exit(0)

# The test needs the SIGALRM signal to be available, so we can't use
# the default signal set which doesn't include it.
if 'SIGALRM' not in signal.__dict__:
    print('Test skipped: SIGALRM not available')
    sys.exit(0)

# Some platforms (e.g. SunOS 5.11) don't support ITIMER_REAL.
if 'ITIMER_REAL' not in signal.__dict__:
    print('Test skipped: ITIMER_REAL not available')
    sys.exit(0)

signal.signal(signal.SIGALRM, lambda signum, frame
