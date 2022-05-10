import signal
# Test signal.setitimer and signal.getitimer
# (not supported on all platforms)

print 'Checking signal.setitimer'

timer = signal.ITIMER_REAL
secs = 0.05

def handler(signum, frame):
    print 'exiting'
    sys.exit()

signal.signal(signal.SIGALRM, handler)

old = signal.setitimer(timer, secs)
print 'old', old

# Wait for the alarm
time.sleep(2)
print 'no alarm'

signal.setitimer(timer, 0)
print 'done'
