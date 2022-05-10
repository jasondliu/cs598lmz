import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Alarm'
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.25)

for i in range(10):
    print i
    time.sleep(1)

print 'Done'
