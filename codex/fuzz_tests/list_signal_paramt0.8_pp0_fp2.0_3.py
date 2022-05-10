import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

start = time.time()
while delays:
    signal.pause()

print('%s secs' % (time.time() - start))
</code>
When I run this script, it only does about 1/4 of the calls, and it takes about 60 seconds.
Back to the original description of the problem, the scenario is essentially this:

Set up a bunch of timers.
The timer fires some Python code.
The code says: "I'm done, please re-arm this timer".

I have an additional requirement that the timers can be arbitrary times, so I can't just have a thread sleep on a condition.


A:

I think you can use Twisted framework.

