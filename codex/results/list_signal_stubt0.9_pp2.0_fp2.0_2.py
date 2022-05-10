import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        print('Done.')

if __name__ == '__main__':
    handler()
    signal.signal(signal.SIGALRM, handler)
    sleep_inf()
</code>


A:

I have been looking in bug tracker and I have found that this bug was fixed in PyCharm 2018.1. Some users are still bothered by it from time to time and JetBrains is still working on it. I hope this issue will be fixed in newer version of PyCharm.

