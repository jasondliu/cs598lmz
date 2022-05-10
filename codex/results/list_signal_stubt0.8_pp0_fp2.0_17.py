import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

sign = 0  # 1 for +, -1 for -
accum = 0

while True:
    sign *= -1
    accum += sign
</code>
With that said, I have never done this and do not know what will happen.

