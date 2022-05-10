import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        simulate(foo=1,bar=2)


def simulate(foo, bar, baz=None):
    print(foo, bar, baz)

signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    signal.pause()
</code>

