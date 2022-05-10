import signal
# Test signal.setitimer
#
# This test is a bit tricky.  The test will run for a few seconds,
# then the timer will fire and the test will exit.  The timer is
# set to fire every second.  The test will check that the timer
# fired at least twice.

def handler(signum, frame):
    print 'handler'

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 1, 1)

count = 0
while 1:
    count = count + 1
    print 'count', count
    time.sleep(1)

print 'FAILED'
