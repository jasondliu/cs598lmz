import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print delays[0]
        return
    if signum is not None and frame is not None:
        print('Signal processing complete')
    signal.signal(signal.SIGALRM, signal.SIG_DFL)

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while delays:
        signal.pause()
</code>
I am puzzled by two things:

The output list (due to <code>print delays[0]</code>) doesn't make sense to me:
<code>1.009876e-06
2.944040e-06
3.765313e-06
4.857667e-06
5.278806e-06
5.997175e-06
7.392505e-06
8.425042e-06
9.100397e-06
9.823
