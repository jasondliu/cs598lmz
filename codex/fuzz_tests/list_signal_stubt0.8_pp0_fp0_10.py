import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        sys.exit(0)

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)

while True:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    if not line:
        break
    else:
        print '%05d %s' % (N - len(delays), line.strip())
