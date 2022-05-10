import signal
# Test signal.setitimer()
#
# This test is known to fail on some systems (including FreeBSD)
# because the signal handler is not called at the expected time.
#
# The test is disabled by default.  To enable it, run this script
# with the --enable option.

import sys
import time

def handler(signum, frame):
    print "handler"
    sys.exit(0)

if __name__ == '__main__':
    if not sys.argv[1:] or sys.argv[1] != '--enable':
        sys.exit(0)

    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0)
    while 1:
        time.sleep(1)
