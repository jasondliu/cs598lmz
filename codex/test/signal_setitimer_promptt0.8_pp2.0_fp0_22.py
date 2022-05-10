import signal
# Test signal.setitimer()
#
# The test is intended to check that signal.setitimer() works reliably.
#
# The signal.setitimer() function is told to send a SIGALRM signal to the
# current process after 1 second.  We then wait for 5 seconds, and expect to
# receive 4 SIGALRM signals.  If any signal is received of a different type, we
# fail the test.  If the signal handler is called fewer than 4 times the test
# also fails.

import os, sys, time, traceback

def alarm_received(n, frame):
    if n != signal.SIGALRM:
        print("FAIL: wrong signal:", n)
        sys.exit(1)
    global alarm_calls
    alarm_calls += 1

alarm_calls = 0
signal.signal(signal.SIGALRM, alarm_received)

signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)
start_time = time.time()
