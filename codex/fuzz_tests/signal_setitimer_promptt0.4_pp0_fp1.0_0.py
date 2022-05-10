import signal
# Test signal.setitimer()
#
# This test does not work on Windows.

import time
import sys

if sys.platform == 'win32':
    raise SystemExit("test skipped on Windows")

def handler(signum, frame):
    print("alarm")
    raise SystemExit

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)
time.sleep(1)
print("no alarm")
