import signal
# Test signal.setitimer() and signal.getitimer()

def alarm_handler(signum, frame):
    print 'got alarm'

signal.signal(signal.SIGALRM, alarm_handler)

signal.setitimer(signal.ITIMER_REAL, 1)

print 'sleeping'
signal.pause()
print 'done'
