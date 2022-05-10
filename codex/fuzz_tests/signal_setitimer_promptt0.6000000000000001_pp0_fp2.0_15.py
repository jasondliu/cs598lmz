import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Alarm!'

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# This should print "Alarm!" ten times
for i in range(10):
    print 'Waiting...'
    time.sleep(0.5)

# Kill the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

print 'Done.'
