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

def loop(count):
    while count &gt; 0:
        count -= 1

count = 1000000
loop(count)

print 'Total time: %.3f' % (time.time() - t0)
</code>
This results in:
<code>Total time: 5.917
</code>
The <code>while</code> loop finishes in about 5.917 seconds.

