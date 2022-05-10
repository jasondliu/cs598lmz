import signal
# Test signal.setitimer()
#
# This test is not very good.  It just makes sure that the call doesn't
# crash.  It doesn't even check that the timer actually fires.

def handler(signum, frame):
    print "handler"

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while 1:
    time.sleep(1)
