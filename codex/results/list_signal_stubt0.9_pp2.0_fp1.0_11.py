import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("done!")
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

signal.signal(signal.SIGALRM, handler)
handler()
while delays:
    signal.pause()
</code>
That being said, I've found this approach to be non-ideal for solving this sort of problem. I'm biased, but I would recommend using gevent; Note that periodic timers are the first-class citizens of the <code>gevent.Greenlet</code> class:
<code>import gevent
from gevent.queue import Queue

def worker(q):
    for delay in iter(q.get, None):
        gevent.sleep(delay)
        print("done!")

q = Queue()
greenlet = gevent.spawn(worker, q)

for delay in [1e-6 + random.random() * 2e-5 for i in range(10000)]:
    q.put(delay)

greenlet.join()
</code>

