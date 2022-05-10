import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)
        print('{0} triggers remaining'.format(len(delays)), file=sys.stderr)
    else:
        signal.setitimer(signal.ITIMER_REAL, 0, 0)
        sys.stderr.write('\n')
        sys.exit(1)


signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)
print('Press Ctrl-C to quit', file=sys.stderr)
while True:
    time.sleep(1)
