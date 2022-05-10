import signal
# Test signal.setitimer
#
# This test is expected to run for a few seconds, and then exit
# with a SIGALRM signal.

def handler(signum, frame):
    print "Got signal", signum
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass
