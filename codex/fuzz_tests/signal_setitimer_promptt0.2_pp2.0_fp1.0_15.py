import signal
# Test signal.setitimer()
#
# This test is Linux-specific.
#
# The test is a bit tricky.  It sets up a signal handler for SIGALRM,
# then sets up a timer to send SIGALRM every second.  The signal
# handler prints a message, then sets up a timer to send SIGALRM every
# half second.  The signal handler for SIGALRM is set to None, so the
# signal will be ignored.  The test is successful if no SIGALRM is
# received after the first one.

def handler(signum, frame):
    print("handler")
    signal.setitimer(signal.ITIMER_REAL, 0.5)
    signal.signal(signal.SIGALRM, None)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1.0)

while True:
    time.sleep(1)
