import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

if hasattr(signal, 'pthread_sigmask'):
    print('Testing pthread_sigmask(2).')
    signal.pthread_sigmask(signal.SIG_BLOCK, [signal.SIGALRM])

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop())

while signal.getitimer(signal.ITIMER_REAL)[0] > 0:
    time.sleep(0.002)

assert len(delays) == 0

print('OK')
