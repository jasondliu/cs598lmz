import signal
# Test signal.setitimer() by setting a timer to go off in 1 second and
# then blocking for 2 seconds.  The timer should go off while we're
# blocked.

def handler(signum, frame):
    print 'Alarm went off'
    signal.alarm(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

time.sleep(2)
print 'Done'
