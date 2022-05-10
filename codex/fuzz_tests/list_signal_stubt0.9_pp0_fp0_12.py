import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

print 'Setting up', N, 'timers'
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print 'Cleanup (%d delays left)' % len(delays)
