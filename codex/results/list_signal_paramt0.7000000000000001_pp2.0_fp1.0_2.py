import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>
The idea is to set the next timer in the handler.  You can do similar things with other timing mechanisms, like <code>time.sleep</code> or <code>asyncio</code>.

