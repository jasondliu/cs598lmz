import signal
# Test signal.setitimer.

signal.setitimer(signal.ITIMER_REAL, 2, 0)

def handler(signum, frame):
    print "handler", signum, frame

signal.signal(signal.SIGALRM, handler)

# Sleeps are used to make sure the signal gets handled.

print "setting ITIMER_REAL to 1,2"
signal.setitimer(signal.ITIMER_REAL, 1, 2)
sleep(3)
print "setting ITIMER_REAL to 2,3"
signal.setitimer(signal.ITIMER_REAL, 2, 3)
sleep(5)
print "setting ITIMER_REAL to 0,0"
signal.setitimer(signal.ITIMER_REAL, 0, 0)
sleep(5)
