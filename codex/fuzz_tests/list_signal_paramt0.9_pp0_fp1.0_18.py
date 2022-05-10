import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)
    else:
        sys.stderr.write('done\n')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)

# signal.alarm(1)
# signal.alarm(0)
# signal.alarm(5)

print('Looping until signal happens')
while delays:
    pass
