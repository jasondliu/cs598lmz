import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
signal.signal(signal.SIGALRM, handler)

while delays:
    signal.pause()
</code>
This program runs at the full speed of the hardware, however, the cost of each callback is high (31 μs on my machine), and it's the same for both approaches
(I measured the callback time of approach 1 to be 32 μs, and the sum of callback + timer delays to be 1e-4 + random.random() * 2e-4, i.e 31.5 μs in average).
So the question is: is there a way to achieve a callback cost of 0 (or as low as possible)?
Note: I know that even if the callback cost is minimized, the cost of doing stuff in it (in the "while True" approach) can still be high, however, the only purpose of callbacks in these approaches is to update some variables and notify the main thread when it's time to wake up, and the callback cost is
