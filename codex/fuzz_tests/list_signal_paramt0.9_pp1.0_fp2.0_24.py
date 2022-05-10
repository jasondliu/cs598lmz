import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        raise SystemExit()

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, handler)
    
    random.seed(142)
    delays.sort()
    handler()
    signal.pause()
