import signal
# Test signal.setitimer

# This test is expected to fail under Windows.

if sys.platform in ('win32', 'os2emx'):
    raise test_support.TestSkipped, "SIGALRM not supported by Windows"

import time

def alarm_received(n, stack):
    print "SIGALRM received"
    raise SystemExit

def call_itimer():
    signal.signal(signal.SIGALRM, alarm_received)
    signal.setitimer(signal.ITIMER_REAL, 0.2)
    print "Sleeping..."
    time.sleep(1.0)
    print "Done."

# call without itimer:
call_itimer()

# call with itimer:
support.run_with_tz('EST+05EDT,M4.1.0,M10.5.0', call_itimer)
