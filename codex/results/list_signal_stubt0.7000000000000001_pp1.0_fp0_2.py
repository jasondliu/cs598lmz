import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('Done.')

if __name__ == '__main__':
    signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)
    signal.signal(signal.SIGALRM, handler)
    while delays:
        time.sleep(0.1)
