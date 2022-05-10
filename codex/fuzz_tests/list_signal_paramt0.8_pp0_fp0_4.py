import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, 0)
    else:
        print('\nDone')

t_last = time()
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
while True:
    t_diff = time() - t_last
    t_last = time()
    sample = random.random() * t_diff * 10 * 1000
    print('\rSample: {:.2f}ms'.format(sample), end='')
