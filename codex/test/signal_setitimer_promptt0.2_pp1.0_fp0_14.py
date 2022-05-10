import signal
# Test signal.setitimer()
#
# This test is Linux-specific.
#
# This test is not run by default.  To run it, do:
#
#   python test_signal.py test_setitimer
#
# The test will run for about 10 seconds.  If it succeeds, it will print
# "OK".  If it fails, it will print "FAIL".
#
# The test works by setting a timer to fire every second.  The signal
# handler increments a counter.  The test passes if the counter is
# incremented 10 times.

def handler(signum, frame):
    global counter
    counter += 1

signal.signal(signal.SIGALRM, handler)

counter = 0
signal.setitimer(signal.ITIMER_REAL, 1, 1)

# Wait for 10 seconds.  If the counter is incremented 10 times, the test
# passes.  If the counter is incremented less than 10 times, the test
# fails.  If the counter is incremented more than 10 times, the test
# fails.

time.sleep
