import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.ITIMER_REAL, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    pass
</code>
If you want to do this for the whole system, not just Python, you can use the <code>tpid</code> extension module to get a thread ID, then use <code>c</code>'s <code>signal.pthread_kill()</code> or a corresponding function and <code>os.sched_yield()</code> to insert <code>pthread_yield()</code> calls between each thread in your process.  That would work on both Linux and Windows (using a different mechanism).

