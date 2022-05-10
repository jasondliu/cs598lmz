import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    print '%s:%s' % (signum, frame)

signal.signal(signal.SIGALRM, handler)

print 'Setting itimer'
signal.setitimer(signal.ITIMER_REAL, delays.pop())

print 'Waiting'
while delays:
    time.sleep(1)

print 'Done'
